---
url: https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#how-to-add-semantic-search-to-your-agents-memory)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add semantic search to your agent's memory 

[ ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/?q= "Share")

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
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
          * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
          * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * Memory  Memory 
            * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
            * [ How to manage conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/)
            * [ How to delete messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/)
            * [ How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/)
            * How to add semantic search to your agent's memory  [ How to add semantic search to your agent's memory  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/) Table of contents 
              * [ Using in your agent  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#using-in-your-agent)
              * [ Using in create_react_agent  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#using-in-create_react_agent)
              * [ Advanced Usage  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#advanced-usage)
                * [ Multi-vector indexing  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#multi-vector-indexing)
                * [ Override fields at storage time  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#override-fields-at-storage-time)
                * [ Disable Indexing for Specific Memories  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#disable-indexing-for-specific-memories)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
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

  * [ Using in your agent  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#using-in-your-agent)
  * [ Using in create_react_agent  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#using-in-create_react_agent)
  * [ Advanced Usage  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#advanced-usage)
    * [ Multi-vector indexing  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#multi-vector-indexing)
    * [ Override fields at storage time  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#override-fields-at-storage-time)
    * [ Disable Indexing for Specific Memories  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#disable-indexing-for-specific-memories)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/memory/semantic-search.ipynb "Edit this page")

# How to add semantic search to your agent's memory[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#how-to-add-semantic-search-to-your-agents-memory "Permanent link")

This guide shows how to enable semantic search in your agent's memory store. This lets search for items in the store by semantic similarity.

Tip

This guide assumes familiarity with the [memory in LangGraph](https://langchain-ai.github.io/langgraph/concepts/memory/).

First, install this guide's prerequisites.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-0-2)%pip install -U langgraph langchain-openai langchain

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Next, create the store with an [index configuration](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig). By default, stores are configured without semantic/vector search. You can opt in to indexing items when creating the store by providing an [IndexConfig](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig) to the store's constructor. If your store class does not implement this interface, or if you do not pass in an index configuration, semantic search is disabled, and all `index` arguments passed to `put` or `aput` will have no effect. Below is an example.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-1)fromlangchain.embeddingsimport init_embeddings
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-2)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-4)# Create store with semantic search enabled
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-5)embeddings = init_embeddings("openai:text-embedding-3-small")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-6)store = InMemoryStore(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-7)  index={
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-8)    "embed": embeddings,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-9)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-10)  }
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-2-11))

```


API Reference: [init_embeddings](https://python.langchain.com/api_reference/langchain/embeddings/langchain.embeddings.base.init_embeddings.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-3-1)/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/ipykernel_83572/2318027494.py:5: LangChainBetaWarning: The function `init_embeddings` is in beta. It is actively being worked on, so the API may change.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-3-2) embeddings = init_embeddings("openai:text-embedding-3-small")

```


Now let's store some memories: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-4-1)# Store some memories
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-4-2)store.put(("user_123", "memories"), "1", {"text": "I love pizza"})
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-4-3)store.put(("user_123", "memories"), "2", {"text": "I prefer Italian food"})
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-4-4)store.put(("user_123", "memories"), "3", {"text": "I don't like spicy food"})
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-4-5)store.put(("user_123", "memories"), "3", {"text": "I am studying econometrics"})
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-4-6)store.put(("user_123", "memories"), "3", {"text": "I am a plumber"})

```


Search memories using natural language:

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-5-1)# Find memories about food preferences
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-5-2)memories = store.search(("user_123", "memories"), query="I like food?", limit=5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-5-4)for memory in memories:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-5-5)  print(f'Memory: {memory.value["text"]} (similarity: {memory.score})')

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-6-1)Memory: I prefer Italian food (similarity: 0.46482669521168163)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-6-2)Memory: I love pizza (similarity: 0.35514845174380766)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-6-3)Memory: I am a plumber (similarity: 0.155698702336571)

```


## Using in your agent[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#using-in-your-agent "Permanent link")

Add semantic search to any node by injecting the store.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-1)fromtypingimport Optional
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-3)fromlangchain.chat_modelsimport init_chat_model
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-4)fromlanggraph.store.baseimport BaseStore
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-6)fromlanggraph.graphimport START, MessagesState, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-8)llm = init_chat_model("openai:gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-11)defchat(state, *, store: BaseStore):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-12)  # Search based on user's last message
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-13)  items = store.search(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-14)    ("user_123", "memories"), query=state["messages"][-1].content, limit=2
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-15)  )
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-16)  memories = "\n".join(item.value["text"] for item in items)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-17)  memories = f"## Memories of user\n{memories}" if memories else ""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-18)  response = llm.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-19)    [
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-20)      {"role": "system", "content": f"You are a helpful assistant.\n{memories}"},
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-21)      *state["messages"],
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-22)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-23)  )
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-24)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-25)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-27)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-28)builder.add_node(chat)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-29)builder.add_edge(START, "chat")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-30)graph = builder.compile(store=store)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-31)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-32)for message, metadata in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-33)  input={"messages": [{"role": "user", "content": "I'm hungry"}]},
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-34)  stream_mode="messages",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-35)):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-7-36)  print(message.content, end="")

```


API Reference: [init_chat_model](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-8-1)What are you in the mood for? Since you love Italian food and pizza, would you like to order a pizza or try making one at home?

```


## Using in `create_react_agent`[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#using-in-create_react_agent "Permanent link")

Add semantic search to your tool calling agent by injecting the store in the `prompt` function. You can also use the store in a tool to let your agent manually store or search for memories.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-1)importuuid
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-2)fromtypingimport Optional
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-4)fromlangchain.chat_modelsimport init_chat_model
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-5)fromlanggraph.prebuiltimport InjectedStore
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-6)fromlanggraph.store.baseimport BaseStore
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-7)fromtyping_extensionsimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-9)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-10)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-12)defprepare_messages(state, *, store: BaseStore):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-13)  # Search based on user's last message
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-14)  items = store.search(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-15)    ("user_123", "memories"), query=state["messages"][-1].content, limit=2
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-16)  )
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-17)  memories = "\n".join(item.value["text"] for item in items)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-18)  memories = f"## Memories of user\n{memories}" if memories else ""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-19)  return [
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-20)    {"role": "system", "content": f"You are a helpful assistant.\n{memories}"}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-21)  ] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-22)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-23)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-24)# You can also use the store directly within a tool!
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-25)defupsert_memory(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-26)  content: str,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-27)  *,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-28)  memory_id: Optional[uuid.UUID] = None,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-29)  store: Annotated[BaseStore, InjectedStore],
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-30)):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-31)"""Upsert a memory in the database."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-32)  # The LLM can use this tool to store a new memory
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-33)  mem_id = memory_id or uuid.uuid4()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-34)  store.put(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-35)    ("user_123", "memories"),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-36)    key=str(mem_id),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-37)    value={"text": content},
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-38)  )
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-39)  return f"Stored memory {mem_id}"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-40)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-41)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-42)agent = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-43)  init_chat_model("openai:gpt-4o-mini"),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-44)  tools=[upsert_memory],
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-45)  # The 'prompt' function is run to prepare the messages for the LLM. It is called
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-46)  # right before each LLM call
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-47)  prompt=prepare_messages,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-48)  store=store,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-9-49))

```


API Reference: [init_chat_model](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-10-1)for message, metadata in agent.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-10-2)  input={"messages": [{"role": "user", "content": "I'm hungry"}]},
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-10-3)  stream_mode="messages",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-10-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-10-5)  print(message.content, end="")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-11-1)What are you in the mood for? Since you love Italian food and pizza, maybe something in that realm would be great! Would you like suggestions for a specific dish or restaurant?

```


## Advanced Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#advanced-usage "Permanent link")

#### Multi-vector indexing[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#multi-vector-indexing "Permanent link")

Store and search different aspects of memories separately to improve recall or omit certain fields from being indexed.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-1)# Configure store to embed both memory content and emotional context
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-2)store = InMemoryStore(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-3)  index={"embed": embeddings, "dims": 1536, "fields": ["memory", "emotional_context"]}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-4))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-5)# Store memories with different content/emotion pairs
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-6)store.put(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-7)  ("user_123", "memories"),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-8)  "mem1",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-9)  {
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-10)    "memory": "Had pizza with friends at Mario's",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-11)    "emotional_context": "felt happy and connected",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-12)    "this_isnt_indexed": "I prefer ravioli though",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-13)  },
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-14))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-15)store.put(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-16)  ("user_123", "memories"),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-17)  "mem2",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-18)  {
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-19)    "memory": "Ate alone at home",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-20)    "emotional_context": "felt a bit lonely",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-21)    "this_isnt_indexed": "I like pie",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-22)  },
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-23))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-24)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-25)# Search focusing on emotional state - matches mem2
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-26)results = store.search(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-27)  ("user_123", "memories"), query="times they felt isolated", limit=1
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-28))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-29)print("Expect mem 2")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-30)for r in results:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-31)  print(f"Item: {r.key}; Score ({r.score})")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-32)  print(f"Memory: {r.value['memory']}")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-33)  print(f"Emotion: {r.value['emotional_context']}\n")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-34)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-35)# Search focusing on social eating - matches mem1
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-36)print("Expect mem1")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-37)results = store.search(("user_123", "memories"), query="fun pizza", limit=1)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-38)for r in results:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-39)  print(f"Item: {r.key}; Score ({r.score})")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-40)  print(f"Memory: {r.value['memory']}")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-41)  print(f"Emotion: {r.value['emotional_context']}\n")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-42)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-43)print("Expect random lower score (ravioli not indexed)")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-44)results = store.search(("user_123", "memories"), query="ravioli", limit=1)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-45)for r in results:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-46)  print(f"Item: {r.key}; Score ({r.score})")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-47)  print(f"Memory: {r.value['memory']}")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-12-48)  print(f"Emotion: {r.value['emotional_context']}\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-1)Expect mem 2
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-2)Item: mem2; Score (0.5895009051396596)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-3)Memory: Ate alone at home
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-4)Emotion: felt a bit lonely
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-6)Expect mem1
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-7)Item: mem1; Score (0.6207546534134083)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-8)Memory: Had pizza with friends at Mario's
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-9)Emotion: felt happy and connected
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-10)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-11)Expect random lower score (ravioli not indexed)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-12)Item: mem1; Score (0.2686278787315685)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-13)Memory: Had pizza with friends at Mario's
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-13-14)Emotion: felt happy and connected

```


#### Override fields at storage time[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#override-fields-at-storage-time "Permanent link")

You can override which fields to embed when storing a specific memory using `put(..., index=[...fields])`, regardless of the store's default configuration.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-1)store = InMemoryStore(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-2)  index={
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-3)    "embed": embeddings,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-4)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-5)    "fields": ["memory"],
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-6)  } # Default to embed memory field
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-7))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-9)# Store one memory with default indexing
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-10)store.put(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-11)  ("user_123", "memories"),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-12)  "mem1",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-13)  {"memory": "I love spicy food", "context": "At a Thai restaurant"},
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-14))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-15)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-16)# Store another overriding which fields to embed
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-17)store.put(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-18)  ("user_123", "memories"),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-19)  "mem2",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-20)  {"memory": "The restaurant was too loud", "context": "Dinner at an Italian place"},
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-21)  index=["context"], # Override: only embed the context
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-22))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-23)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-24)# Search about food - matches mem1 (using default field)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-25)print("Expect mem1")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-26)results = store.search(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-27)  ("user_123", "memories"), query="what food do they like", limit=1
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-28))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-29)for r in results:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-30)  print(f"Item: {r.key}; Score ({r.score})")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-31)  print(f"Memory: {r.value['memory']}")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-32)  print(f"Context: {r.value['context']}\n")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-33)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-34)# Search about restaurant atmosphere - matches mem2 (using overridden field)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-35)print("Expect mem2")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-36)results = store.search(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-37)  ("user_123", "memories"), query="restaurant environment", limit=1
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-38))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-39)for r in results:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-40)  print(f"Item: {r.key}; Score ({r.score})")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-41)  print(f"Memory: {r.value['memory']}")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-14-42)  print(f"Context: {r.value['context']}\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-1)Expect mem1
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-2)Item: mem1; Score (0.3374968677940555)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-3)Memory: I love spicy food
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-4)Context: At a Thai restaurant
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-6)Expect mem2
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-7)Item: mem2; Score (0.36784461593247436)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-8)Memory: The restaurant was too loud
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-15-9)Context: Dinner at an Italian place

```


#### Disable Indexing for Specific Memories[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#disable-indexing-for-specific-memories "Permanent link")

Some memories shouldn't be searchable by content. You can disable indexing for these while still storing them using `put(..., index=False)`. Example:

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-1)store = InMemoryStore(index={"embed": embeddings, "dims": 1536, "fields": ["memory"]})
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-3)# Store a normal indexed memory
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-4)store.put(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-5)  ("user_123", "memories"),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-6)  "mem1",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-7)  {"memory": "I love chocolate ice cream", "type": "preference"},
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-8))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-10)# Store a system memory without indexing
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-11)store.put(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-12)  ("user_123", "memories"),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-13)  "mem2",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-14)  {"memory": "User completed onboarding", "type": "system"},
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-15)  index=False, # Disable indexing entirely
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-16))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-17)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-18)# Search about food preferences - finds mem1
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-19)print("Expect mem1")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-20)results = store.search(("user_123", "memories"), query="what food preferences", limit=1)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-21)for r in results:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-22)  print(f"Item: {r.key}; Score ({r.score})")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-23)  print(f"Memory: {r.value['memory']}")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-24)  print(f"Type: {r.value['type']}\n")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-25)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-26)# Search about onboarding - won't find mem2 (not indexed)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-27)print("Expect low score (mem2 not indexed)")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-28)results = store.search(("user_123", "memories"), query="onboarding status", limit=1)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-29)for r in results:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-30)  print(f"Item: {r.key}; Score ({r.score})")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-31)  print(f"Memory: {r.value['memory']}")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-16-32)  print(f"Type: {r.value['type']}\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-1)Expect mem1
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-2)Item: mem1; Score (0.32269984224327286)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-3)Memory: I love chocolate ice cream
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-4)Type: preference
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-6)Expect low score (mem2 not indexed)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-7)Item: mem1; Score (0.010241633698527089)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-8)Memory: I love chocolate ice cream
[](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__codelineno-17-9)Type: preference

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/) [ Next  How to add breakpoints  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
