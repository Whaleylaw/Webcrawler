---
url: https://langchain-ai.github.io/langgraph/concepts/multi_agent/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#multi-agent-systems)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Multi-agent Systems 

[ ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/?q= "Share")

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
          * Multi-agent Systems  [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/) Table of contents 
            * [ Multi-agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#multi-agent-architectures)
              * [ Handoffs  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs)
                * [ Handoffs as tools  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs-as-tools)
              * [ Network  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#network)
              * [ Supervisor  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor)
              * [ Supervisor (tool-calling)  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor-tool-calling)
              * [ Hierarchical  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#hierarchical)
              * [ Custom multi-agent workflow  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#custom-multi-agent-workflow)
            * [ Communication between agents  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#communication-between-agents)
              * [ Graph state vs tool calls  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#graph-state-vs-tool-calls)
                * [ Graph state  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#graph-state)
              * [ Different state schemas  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#different-state-schemas)
              * [ Shared message list  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#shared-message-list)
                * [ Share full history  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#share-full-history)
                * [ Share final result  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#share-final-result)
          * [ None  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
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

  * [ Multi-agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#multi-agent-architectures)
    * [ Handoffs  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs)
      * [ Handoffs as tools  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs-as-tools)
    * [ Network  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#network)
    * [ Supervisor  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor)
    * [ Supervisor (tool-calling)  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor-tool-calling)
    * [ Hierarchical  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#hierarchical)
    * [ Custom multi-agent workflow  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#custom-multi-agent-workflow)
  * [ Communication between agents  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#communication-between-agents)
    * [ Graph state vs tool calls  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#graph-state-vs-tool-calls)
      * [ Graph state  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#graph-state)
    * [ Different state schemas  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#different-state-schemas)
    * [ Shared message list  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#shared-message-list)
      * [ Share full history  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#share-full-history)
      * [ Share final result  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#share-final-result)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/multi_agent.md "Edit this page")

# Multi-agent Systems[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#multi-agent-systems "Permanent link")

An [agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#agent-architectures) is _a system that uses an LLM to decide the control flow of an application_. As you develop these systems, they might grow more complex over time, making them harder to manage and scale. For example, you might run into the following problems:

  * agent has too many tools at its disposal and makes poor decisions about which tool to call next
  * context grows too complex for a single agent to keep track of
  * there is a need for multiple specialization areas in the system (e.g. planner, researcher, math expert, etc.)



To tackle these, you might consider breaking your application into multiple smaller, independent agents and composing them into a **multi-agent system**. These independent agents can be as simple as a prompt and an LLM call, or as complex as a [ReAct](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-implementation) agent (and more!).

The primary benefits of using multi-agent systems are:

  * **Modularity** : Separate agents make it easier to develop, test, and maintain agentic systems.
  * **Specialization** : You can create expert agents focused on specific domains, which helps with the overall system performance.
  * **Control** : You can explicitly control how agents communicate (as opposed to relying on function calling).



## Multi-agent architectures[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#multi-agent-architectures "Permanent link")

![](https://langchain-ai.github.io/langgraph/concepts/img/multi_agent/architectures.png)

There are several ways to connect agents in a multi-agent system:

  * **Network** : each agent can communicate with [every other agent](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/). Any agent can decide which other agent to call next.
  * **Supervisor** : each agent communicates with a single [supervisor](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/) agent. Supervisor agent makes decisions on which agent should be called next.
  * **Supervisor (tool-calling)** : this is a special case of supervisor architecture. Individual agents can be represented as tools. In this case, a supervisor agent uses a tool-calling LLM to decide which of the agent tools to call, as well as the arguments to pass to those agents.
  * **Hierarchical** : you can define a multi-agent system with [a supervisor of supervisors](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/). This is a generalization of the supervisor architecture and allows for more complex control flows.
  * **Custom multi-agent workflow** : each agent communicates with only a subset of agents. Parts of the flow are deterministic, and only some agents can decide which other agents to call next.



### Handoffs[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs "Permanent link")

In multi-agent architectures, agents can be represented as graph nodes. Each agent node executes its step(s) and decides whether to finish execution or route to another agent, including potentially routing to itself (e.g., running in a loop). A common pattern in multi-agent interactions is handoffs, where one agent hands off control to another. Handoffs allow you to specify:

  * **destination** : target agent to navigate to (e.g., name of the node to go to)
  * **payload** : [information to pass to that agent](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#communication-between-agents) (e.g., state update)



To implement handoffs in LangGraph, agent nodes can return `Command`[](https://langchain-ai.github.io/langgraph/concepts/low_level/#command) object that allows you to combine both control flow and state updates:

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-1)defagent(state) -> Command[Literal["agent", "another_agent"]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-2)  # the condition for routing/halting can be anything, e.g. LLM tool call / structured output, etc.
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-3)  goto = get_next_agent(...) # 'agent' / 'another_agent'
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-4)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-5)    # Specify which agent to call next
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-6)    goto=goto,
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-7)    # Update the graph state
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-8)    update={"my_state_key": "my_state_value"}
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-0-9)  )

```


In a more complex scenario where each agent node is itself a graph (i.e., a [subgraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs)), a node in one of the agent subgraphs might want to navigate to a different agent. For example, if you have two agents, `alice` and `bob` (subgraph nodes in a parent graph), and `alice` needs to navigate to `bob`, you can set `graph=Command.PARENT` in the `Command` object:

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-1-1)defsome_node_inside_alice(state)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-1-2)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-1-3)    goto="bob",
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-1-4)    update={"my_state_key": "my_state_value"},
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-1-5)    # specify which graph to navigate to (defaults to the current graph)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-1-6)    graph=Command.PARENT,
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-1-7)  )

```


Note

If you need to support visualization for subgraphs communicating using `Command(graph=Command.PARENT)` you would need to wrap them in a node function with `Command` annotation, e.g. instead of this:

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-2-1)builder.add_node(alice)

```


you would need to do this:

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-3-1)defcall_alice(state) -> Command[Literal["bob"]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-3-2)  return alice.invoke(state)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-3-4)builder.add_node("alice", call_alice)

```


#### Handoffs as tools[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs-as-tools "Permanent link")

One of the most common agent types is a ReAct-style tool-calling agents. For those types of agents, a common pattern is wrapping a handoff in a tool call, e.g.:

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-4-1)deftransfer_to_bob(state):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-4-2)"""Transfer to bob."""
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-4-3)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-4-4)    goto="bob",
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-4-5)    update={"my_state_key": "my_state_value"},
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-4-6)    graph=Command.PARENT,
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-4-7)  )

```


This is a special case of updating the graph state from tools where in addition the state update, the control flow is included as well.

Important

If you want to use tools that return `Command`, you can either use prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) / `ToolNode`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) components, or implement your own tool-executing node that collects `Command` objects returned by the tools and returns a list of them, e.g.:

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-5-1)defcall_tools(state):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-5-2)  ...
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-5-3)  commands = [tools_by_name[tool_call["name"]].invoke(tool_call) for tool_call in tool_calls]
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-5-4)  return commands

```


Let's now take a closer look at the different multi-agent architectures.

### Network[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#network "Permanent link")

In this architecture, agents are defined as graph nodes. Each agent can communicate with every other agent (many-to-many connections) and can decide which agent to call next. This architecture is good for problems that do not have a clear hierarchy of agents or a specific sequence in which agents should be called.

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-3)fromlanggraph.graphimport StateGraph, MessagesState, START, END
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-5)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-7)defagent_1(state: MessagesState) -> Command[Literal["agent_2", "agent_3", END]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-8)  # you can pass relevant parts of the state to the LLM (e.g., state["messages"])
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-9)  # to determine which agent to call next. a common pattern is to call the model
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-10)  # with a structured output (e.g. force it to return an output with a "next_agent" field)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-11)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-12)  # route to one of the agents or exit based on the LLM's decision
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-13)  # if the LLM returns "__end__", the graph will finish execution
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-14)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-15)    goto=response["next_agent"],
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-16)    update={"messages": [response["content"]]},
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-17)  )
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-19)defagent_2(state: MessagesState) -> Command[Literal["agent_1", "agent_3", END]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-20)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-21)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-22)    goto=response["next_agent"],
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-23)    update={"messages": [response["content"]]},
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-24)  )
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-25)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-26)defagent_3(state: MessagesState) -> Command[Literal["agent_1", "agent_2", END]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-27)  ...
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-28)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-29)    goto=response["next_agent"],
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-30)    update={"messages": [response["content"]]},
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-31)  )
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-32)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-33)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-34)builder.add_node(agent_1)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-35)builder.add_node(agent_2)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-36)builder.add_node(agent_3)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-37)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-38)builder.add_edge(START, "agent_1")
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-6-39)network = builder.compile()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

### Supervisor[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor "Permanent link")

In this architecture, we define agents as nodes and add a supervisor node (LLM) that decides which agent nodes should be called next. We use `Command`[](https://langchain-ai.github.io/langgraph/concepts/low_level/#command) to route execution to the appropriate agent node based on supervisor's decision. This architecture also lends itself well to running multiple agents in parallel or using [map-reduce](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/) pattern.

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-3)fromlanggraph.graphimport StateGraph, MessagesState, START, END
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-5)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-7)defsupervisor(state: MessagesState) -> Command[Literal["agent_1", "agent_2", END]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-8)  # you can pass relevant parts of the state to the LLM (e.g., state["messages"])
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-9)  # to determine which agent to call next. a common pattern is to call the model
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-10)  # with a structured output (e.g. force it to return an output with a "next_agent" field)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-11)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-12)  # route to one of the agents or exit based on the supervisor's decision
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-13)  # if the supervisor returns "__end__", the graph will finish execution
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-14)  return Command(goto=response["next_agent"])
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-16)defagent_1(state: MessagesState) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-17)  # you can pass relevant parts of the state to the LLM (e.g., state["messages"])
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-18)  # and add any additional logic (different models, custom prompts, structured output, etc.)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-19)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-20)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-21)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-22)    update={"messages": [response]},
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-23)  )
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-24)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-25)defagent_2(state: MessagesState) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-26)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-27)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-28)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-29)    update={"messages": [response]},
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-30)  )
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-31)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-32)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-33)builder.add_node(supervisor)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-34)builder.add_node(agent_1)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-35)builder.add_node(agent_2)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-36)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-37)builder.add_edge(START, "supervisor")
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-38)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-7-39)supervisor = builder.compile()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

Check out this [tutorial](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/) for an example of supervisor multi-agent architecture.

### Supervisor (tool-calling)[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor-tool-calling "Permanent link")

In this variant of the [supervisor](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor) architecture, we define individual agents as **tools** and use a tool-calling LLM in the supervisor node. This can be implemented as a [ReAct](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-implementation)-style agent with two nodes — an LLM node (supervisor) and a tool-calling node that executes tools (agents in this case).

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-3)fromlanggraph.prebuiltimport InjectedState, create_react_agent
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-5)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-7)# this is the agent function that will be called as tool
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-8)# notice that you can pass the state to the tool via InjectedState annotation
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-9)defagent_1(state: Annotated[dict, InjectedState]):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-10)  # you can pass relevant parts of the state to the LLM (e.g., state["messages"])
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-11)  # and add any additional logic (different models, custom prompts, structured output, etc.)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-12)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-13)  # return the LLM response as a string (expected tool response format)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-14)  # this will be automatically turned to ToolMessage
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-15)  # by the prebuilt create_react_agent (supervisor)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-16)  return response.content
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-17)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-18)defagent_2(state: Annotated[dict, InjectedState]):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-19)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-20)  return response.content
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-21)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-22)tools = [agent_1, agent_2]
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-23)# the simplest way to build a supervisor w/ tool-calling is to use prebuilt ReAct agent graph
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-24)# that consists of a tool-calling LLM node (i.e. supervisor) and a tool-executing node
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-8-25)supervisor = create_react_agent(model, tools)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

### Hierarchical[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#hierarchical "Permanent link")

As you add more agents to your system, it might become too hard for the supervisor to manage all of them. The supervisor might start making poor decisions about which agent to call next, the context might become too complex for a single supervisor to keep track of. In other words, you end up with the same problems that motivated the multi-agent architecture in the first place.

To address this, you can design your system _hierarchically_. For example, you can create separate, specialized teams of agents managed by individual supervisors, and a top-level supervisor to manage the teams.

```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-3)fromlanggraph.graphimport StateGraph, MessagesState, START, END
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-4)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-5)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-7)# define team 1 (same as the single supervisor example above)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-8)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-9)defteam_1_supervisor(state: MessagesState) -> Command[Literal["team_1_agent_1", "team_1_agent_2", END]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-10)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-11)  return Command(goto=response["next_agent"])
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-12)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-13)defteam_1_agent_1(state: MessagesState) -> Command[Literal["team_1_supervisor"]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-14)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-15)  return Command(goto="team_1_supervisor", update={"messages": [response]})
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-16)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-17)defteam_1_agent_2(state: MessagesState) -> Command[Literal["team_1_supervisor"]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-18)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-19)  return Command(goto="team_1_supervisor", update={"messages": [response]})
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-20)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-21)team_1_builder = StateGraph(Team1State)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-22)team_1_builder.add_node(team_1_supervisor)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-23)team_1_builder.add_node(team_1_agent_1)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-24)team_1_builder.add_node(team_1_agent_2)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-25)team_1_builder.add_edge(START, "team_1_supervisor")
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-26)team_1_graph = team_1_builder.compile()
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-27)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-28)# define team 2 (same as the single supervisor example above)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-29)classTeam2State(MessagesState):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-30)  next: Literal["team_2_agent_1", "team_2_agent_2", "__end__"]
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-31)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-32)defteam_2_supervisor(state: Team2State):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-33)  ...
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-34)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-35)defteam_2_agent_1(state: Team2State):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-36)  ...
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-37)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-38)defteam_2_agent_2(state: Team2State):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-39)  ...
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-40)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-41)team_2_builder = StateGraph(Team2State)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-42)...
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-43)team_2_graph = team_2_builder.compile()
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-44)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-45)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-46)# define top-level supervisor
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-47)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-48)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-49)deftop_level_supervisor(state: MessagesState) -> Command[Literal["team_1_graph", "team_2_graph", END]]:
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-50)  # you can pass relevant parts of the state to the LLM (e.g., state["messages"])
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-51)  # to determine which team to call next. a common pattern is to call the model
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-52)  # with a structured output (e.g. force it to return an output with a "next_team" field)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-53)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-54)  # route to one of the teams or exit based on the supervisor's decision
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-55)  # if the supervisor returns "__end__", the graph will finish execution
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-56)  return Command(goto=response["next_team"])
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-57)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-58)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-59)builder.add_node(top_level_supervisor)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-60)builder.add_node("team_1_graph", team_1_graph)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-61)builder.add_node("team_2_graph", team_2_graph)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-62)builder.add_edge(START, "top_level_supervisor")
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-63)builder.add_edge("team_1_graph", "top_level_supervisor")
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-64)builder.add_edge("team_2_graph", "top_level_supervisor")
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-9-65)graph = builder.compile()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

### Custom multi-agent workflow[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#custom-multi-agent-workflow "Permanent link")

In this architecture we add individual agents as graph nodes and define the order in which agents are called ahead of time, in a custom workflow. In LangGraph the workflow can be defined in two ways:

  * **Explicit control flow (normal edges)** : LangGraph allows you to explicitly define the control flow of your application (i.e. the sequence of how agents communicate) explicitly, via [normal graph edges](https://langchain-ai.github.io/langgraph/concepts/low_level/#normal-edges). This is the most deterministic variant of this architecture above — we always know which agent will be called next ahead of time.

  * **Dynamic control flow (Command)** : in LangGraph you can allow LLMs to decide parts of your application control flow. This can be achieved by using `Command`[](https://langchain-ai.github.io/langgraph/concepts/low_level/#command). A special case of this is a [supervisor tool-calling](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor-tool-calling) architecture. In that case, the tool-calling LLM powering the supervisor agent will make decisions about the order in which the tools (agents) are being called.




```
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-2)fromlanggraph.graphimport StateGraph, MessagesState, START
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-4)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-6)defagent_1(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-7)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-8)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-10)defagent_2(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-11)  response = model.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-12)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-14)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-15)builder.add_node(agent_1)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-16)builder.add_node(agent_2)
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-17)# define the flow explicitly
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-18)builder.add_edge(START, "agent_1")
[](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__codelineno-10-19)builder.add_edge("agent_1", "agent_2")

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

## Communication between agents[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#communication-between-agents "Permanent link")

The most important thing when building multi-agent systems is figuring out how the agents communicate. There are few different considerations:

  * Do agents communicate via [**via graph state or via tool calls**](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#graph-state-vs-tool-calls)?
  * What if two agents have [**different state schemas**](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#different-state-schemas)?
  * How to communicate over a [**shared message list**](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#shared-message-list)?



### Graph state vs tool calls[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#graph-state-vs-tool-calls "Permanent link")

What is the "payload" that is being passed around between agents? In most of the architectures discussed above the agents communicate via the [graph state](https://langchain-ai.github.io/langgraph/concepts/low_level/#state). In the case of the [supervisor with tool-calling](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor-tool-calling), the payloads are tool call arguments.

![](https://langchain-ai.github.io/langgraph/concepts/img/multi_agent/request.png)

#### Graph state[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#graph-state "Permanent link")

To communicate via graph state, individual agents need to be defined as [graph nodes](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes). These can be added as functions or as entire [subgraphs](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs). At each step of the graph execution, agent node receives the current state of the graph, executes the agent code and then passes the updated state to the next nodes.

Typically agent nodes share a single [state schema](https://langchain-ai.github.io/langgraph/concepts/low_level/#schema). However, you might want to design agent nodes with [different state schemas](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#different-state-schemas).

### Different state schemas[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#different-state-schemas "Permanent link")

An agent might need to have a different state schema from the rest of the agents. For example, a search agent might only need to keep track of queries and retrieved documents. There are two ways to achieve this in LangGraph:

  * Define [subgraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs) agents with a separate state schema. If there are no shared state keys (channels) between the subgraph and the parent graph, it’s important to [add input / output transformations](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/) so that the parent graph knows how to communicate with the subgraphs.
  * Define agent node functions with a [private input state schema](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/) that is distinct from the overall graph state schema. This allows passing information that is only needed for executing that particular agent.



### Shared message list[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#shared-message-list "Permanent link")

The most common way for the agents to communicate is via a shared state channel, typically a list of messages. This assumes that there is always at least a single channel (key) in the state that is shared by the agents. When communicating via a shared message list there is an additional consideration: should the agents [share the full history](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#share-full-history) of their thought process or only [the final result](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#share-final-result)?

![](https://langchain-ai.github.io/langgraph/concepts/img/multi_agent/response.png)

#### Share full history[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#share-full-history "Permanent link")

Agents can **share the full history** of their thought process (i.e. "scratchpad") with all other agents. This "scratchpad" would typically look like a [list of messages](https://langchain-ai.github.io/langgraph/concepts/low_level/#why-use-messages). The benefit of sharing full thought process is that it might help other agents make better decisions and improve reasoning ability for the system as a whole. The downside is that as the number of agents and their complexity grows, the "scratchpad" will grow quickly and might require additional strategies for [memory management](https://langchain-ai.github.io/langgraph/concepts/memory/#managing-long-conversation-history).

#### Share final result[¶](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#share-final-result "Permanent link")

Agents can have their own private "scratchpad" and only **share the final result** with the rest of the agents. This approach might work better for systems with many agents or agents that are more complex. In this case, you would need to define agents with [different state schemas](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#different-state-schemas)

For agents called as tools, the supervisor determines the inputs based on the tool schema. Additionally, LangGraph allows [passing state](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#pass-graph-state-to-tools) to individual tools at runtime, so subordinate agents can access parent state, if needed.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/) [ Next  Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
