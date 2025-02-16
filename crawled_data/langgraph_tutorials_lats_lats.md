---
url: https://langchain-ai.github.io/langgraph/tutorials/lats/lats/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#language-agent-tree-search)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Language Agent Tree Search 

[ ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/?q= "Share")

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
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)

Tutorials 
        * [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials#quick-start)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)
        * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
        * Agent Architectures  Agent Architectures 
          * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
          * [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraph/tutorials#multi-agent-systems)
          * [ Planning Agents  ](https://langchain-ai.github.io/langgraph/tutorials#planning-agents)
          * Reflection & Critique  Reflection & Critique 
            * [ Reflection & Critique  ](https://langchain-ai.github.io/langgraph/tutorials#reflection-critique)
            * [ Reflection  ](https://langchain-ai.github.io/langgraph/tutorials/reflection/reflection/)
            * [ Reflexion  ](https://langchain-ai.github.io/langgraph/tutorials/reflexion/reflexion/)
            * [ Tree of Thoughts  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/)
            * Language Agent Tree Search  [ Language Agent Tree Search  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#setup)
              * [ Graph State  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#graph-state)
                * [ The graph state itself  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#the-graph-state-itself)
              * [ Define Language Agent  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#define-language-agent)
                * [ Tools  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#tools)
                * [ Reflection  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#reflection)
                * [ Initial Response  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#initial-response)
                  * [ Starting Node  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#starting-node)
                * [ Candidate Generation  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#candidate-generation)
                  * [ Candidate generation node  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#candidate-generation-node)
              * [ Create Graph  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#create-graph)
              * [ Invoke  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#invoke)
              * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#conclusion)
            * [ Self-Discover Agent  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)
        * [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#setup)
  * [ Graph State  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#graph-state)
    * [ The graph state itself  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#the-graph-state-itself)
  * [ Define Language Agent  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#define-language-agent)
    * [ Tools  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#tools)
    * [ Reflection  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#reflection)
    * [ Initial Response  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#initial-response)
      * [ Starting Node  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#starting-node)
    * [ Candidate Generation  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#candidate-generation)
      * [ Candidate generation node  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#candidate-generation-node)
  * [ Create Graph  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#create-graph)
  * [ Invoke  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#invoke)
  * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#conclusion)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
  5. [ Reflection & Critique  ](https://langchain-ai.github.io/langgraph/tutorials#reflection-critique)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/lats/lats.ipynb "Edit this page")

# Language Agent Tree Search[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#language-agent-tree-search "Permanent link")

[Language Agent Tree Search](https://arxiv.org/abs/2310.04406) (LATS), by Zhou, et. al, is a general LLM agent search algorithm that combines reflection/evaluation and search (specifically monte-carlo trees search) to get achieve better overall task performance compared to similar techniques like ReACT, Reflexion, or Tree of Thoughts.

![LATS diagram]()

It has four main steps:

  1. Select: pick the best next actions based on the aggregate rewards from step (2). Either respond (if a solution is found or the max search depth is reached) or continue searching.
  2. Expand and simulate: select the "best" 5 potential actions to take and execute them in parallel.
  3. Reflect + Evaluate: observe the outcomes of these actions and score the decisions based on reflection (and possibly external feedback)
  4. Backpropagate: update the scores of the root trajectories based on the outcomes.



## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#setup "Permanent link")

Install `langgraph` (for the framework), `langchain_openai` (for the LLM), and `langchain` + `tavily-python` (for the search engine).

We will use tavily search as a tool. You can get an API key [here](https://app.tavily.com/sign-in) or replace with a different tool of your choosing.

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-0-2)%pip install -U --quiet langchain langgraph langchain_openai
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-0-3)%pip install -U --quiet tavily-python

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-5)def_set_if_undefined(var: str) -> None:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-6)  if os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-7)    return
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-8)  os.environ[var] = getpass.getpass(var)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-11)_set_if_undefined("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-1-12)_set_if_undefined("TAVILY_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Graph State[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#graph-state "Permanent link")

LATS is based on a (greedy) Monte-Carlo tree search. For each search steps, it picks the node with the highest "upper confidence bound", which is a metric that balances exploitation (highest average reward) and exploration (lowest visits). Starting from that node, it generates N (5 in this case) new candidate actions to take, and adds them to the tree. It stops searching either when it has generated a valid solution OR when it has reached the maximum number of rollouts (search tree depth).

![Tree Diagram]()

Our LangGraph state will be composed of two items: 1. The root of the search tree 2. The user input

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-1)importmath
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-2)fromcollectionsimport deque
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-3)fromtypingimport Optional
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-5)fromlangchain_core.messagesimport AIMessage, BaseMessage, HumanMessage, ToolMessage
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-7)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-10)classReflection(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-11)  reflections: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-12)    description="The critique and reflections on the sufficiency, superfluency,"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-13)    " and general quality of the response"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-14)  )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-15)  score: int = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-16)    description="Score from 0-10 on the quality of the candidate response.",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-17)    gte=0,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-18)    lte=10,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-19)  )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-20)  found_solution: bool = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-21)    description="Whether the response has fully solved the question or task."
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-22)  )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-23)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-24)  defas_message(self):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-25)    return HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-26)      content=f"Reasoning: {self.reflections}\nScore: {self.score}"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-27)    )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-28)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-29)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-30)  defnormalized_score(self) -> float:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-31)    return self.score / 10.0
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-32)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-33)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-34)classNode:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-35)  def__init__(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-36)    self,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-37)    messages: list[BaseMessage],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-38)    reflection: Reflection,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-39)    parent: Optional["Node"] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-40)  ):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-41)    self.messages = messages
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-42)    self.parent = parent
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-43)    self.children = []
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-44)    self.value = 0
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-45)    self.visits = 0
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-46)    self.reflection = reflection
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-47)    self.depth = parent.depth + 1 if parent is not None else 1
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-48)    self._is_solved = reflection.found_solution if reflection else False
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-49)    if self._is_solved:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-50)      self._mark_tree_as_solved()
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-51)    self.backpropagate(reflection.normalized_score)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-52)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-53)  def__repr__(self) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-54)    return (
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-55)      f"<Node value={self.value}, visits={self.visits},"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-56)      f" solution={self.messages} reflection={self.reflection}/>"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-57)    )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-58)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-59)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-60)  defis_solved(self):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-61)"""If any solutions exist, we can end the search."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-62)    return self._is_solved
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-63)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-64)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-65)  defis_terminal(self):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-66)    return not self.children
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-67)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-68)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-69)  defbest_child_score(self):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-70)"""Return the child with the highest value."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-71)    if not self.children:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-72)      return None
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-73)    return max(self.children, key=lambda child: int(child.is_solved) * child.value)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-74)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-75)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-76)  defheight(self) -> int:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-77)"""Check for how far we've rolled out the tree."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-78)    if self.children:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-79)      return 1 + max([child.height for child in self.children])
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-80)    return 1
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-81)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-82)  defupper_confidence_bound(self, exploration_weight=1.0):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-83)"""Return the UCT score. This helps balance exploration vs. exploitation of a branch."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-84)    if self.parent is None:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-85)      raise ValueError("Cannot obtain UCT from root node")
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-86)    if self.visits == 0:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-87)      return self.value
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-88)    # Encourages exploitation of high-value trajectories
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-89)    average_reward = self.value / self.visits
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-90)    # Encourages exploration of less-visited trajectories
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-91)    exploration_term = math.sqrt(math.log(self.parent.visits) / self.visits)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-92)    return average_reward + exploration_weight * exploration_term
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-93)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-94)  defbackpropagate(self, reward: float):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-95)"""Update the score of this node and its parents."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-96)    node = self
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-97)    while node:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-98)      node.visits += 1
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-99)      node.value = (node.value * (node.visits - 1) + reward) / node.visits
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-100)      node = node.parent
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-101)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-102)  defget_messages(self, include_reflections: bool = True):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-103)    if include_reflections:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-104)      return self.messages + [self.reflection.as_message()]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-105)    return self.messages
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-106)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-107)  defget_trajectory(self, include_reflections: bool = True) -> list[BaseMessage]:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-108)"""Get messages representing this search branch."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-109)    messages = []
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-110)    node = self
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-111)    while node:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-112)      messages.extend(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-113)        node.get_messages(include_reflections=include_reflections)[::-1]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-114)      )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-115)      node = node.parent
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-116)    # Reverse the final back-tracked trajectory to return in the correct order
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-117)    return messages[::-1] # root solution, reflection, child 1, ...
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-118)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-119)  def_get_all_children(self):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-120)    all_nodes = []
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-121)    nodes = deque()
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-122)    nodes.append(self)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-123)    while nodes:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-124)      node = nodes.popleft()
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-125)      all_nodes.extend(node.children)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-126)      for n in node.children:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-127)        nodes.append(n)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-128)    return all_nodes
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-129)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-130)  defget_best_solution(self):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-131)"""Return the best solution from within the current sub-tree."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-132)    all_nodes = [self] + self._get_all_children()
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-133)    best_node = max(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-134)      all_nodes,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-135)      # We filter out all non-terminal, non-solution trajectories
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-136)      key=lambda node: int(node.is_terminal and node.is_solved) * node.value,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-137)    )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-138)    return best_node
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-139)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-140)  def_mark_tree_as_solved(self):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-141)    parent = self.parent
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-142)    while parent:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-143)      parent._is_solved = True
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-2-144)      parent = parent.parent

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html)

#### The graph state itself[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#the-graph-state-itself "Permanent link")

The main component is the tree, represented by the root node.

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-3-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-3-4)classTreeState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-3-5)  # The full tree
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-3-6)  root: Node
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-3-7)  # The original input
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-3-8)  input: str

```


## Define Language Agent[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#define-language-agent "Permanent link")

Our agent will have three primary LLM-powered processes: 1. Reflect: score the action based on the tool response. 2. Initial response: to create the root node and start the search. 3. Expand: generate 5 candidate "next steps" from the best spot in the current tree

For more "Grounded" tool applications (such as code synthesis), you could integrate code execution into the reflection/reward step. This type of external feedback is very useful (though adds complexity to an already complicated example notebook).

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-4-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-4-3)llm = ChatOpenAI(model="gpt-4o")

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

#### Tools[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#tools "Permanent link")

For our example, we will give the language agent a search engine.

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-5-1)fromlangchain_community.tools.tavily_searchimport TavilySearchResults
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-5-2)fromlangchain_community.utilities.tavily_searchimport TavilySearchAPIWrapper
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-5-3)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-5-5)search = TavilySearchAPIWrapper()
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-5-6)tavily_tool = TavilySearchResults(api_wrapper=search, max_results=5)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-5-7)tools = [tavily_tool]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-5-8)tool_node = ToolNode(tools=tools)

```


API Reference: [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html) | [TavilySearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.tavily_search.TavilySearchAPIWrapper.html) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

### Reflection[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#reflection "Permanent link")

The reflection chain will score agent outputs based on the decision and the tool responses. We will call this within the other two nodes.

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-1)fromlangchain_core.output_parsers.openai_toolsimport (
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-2)  JsonOutputToolsParser,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-3)  PydanticToolsParser,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-4))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-5)fromlangchain_core.promptsimport ChatPromptTemplate, MessagesPlaceholder
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-6)fromlangchain_core.runnablesimport chain as as_runnable
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-8)prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-9)  [
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-10)    (
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-11)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-12)      "Reflect and grade the assistant response to the user question below.",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-13)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-14)    ("user", "{input}"),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-15)    MessagesPlaceholder(variable_name="candidate"),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-16)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-17))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-19)reflection_llm_chain = (
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-20)  prompt
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-21)  | llm.bind_tools(tools=[Reflection], tool_choice="Reflection").with_config(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-22)    run_name="Reflection"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-23)  )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-24)  | PydanticToolsParser(tools=[Reflection])
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-25))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-26)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-27)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-28)@as_runnable
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-29)defreflection_chain(inputs) -> Reflection:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-30)  tool_choices = reflection_llm_chain.invoke(inputs)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-31)  reflection = tool_choices[0]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-32)  if not isinstance(inputs["candidate"][-1], AIMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-33)    reflection.found_solution = False
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-6-34)  return reflection

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [MessagesPlaceholder](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html) | [chain](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.chain.html)

### Initial Response[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#initial-response "Permanent link")

We start with a single root node, generated by this first step. It responds to the user input either with a tool invocation or a response.

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-1)fromlangchain_core.prompt_valuesimport ChatPromptValue
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-2)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-4)prompt_template = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-5)  [
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-6)    (
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-7)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-8)      "You are an AI assistant.",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-9)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-10)    ("user", "{input}"),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-11)    MessagesPlaceholder(variable_name="messages", optional=True),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-12)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-13))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-14)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-16)initial_answer_chain = prompt_template | llm.bind_tools(tools=tools).with_config(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-17)  run_name="GenerateInitialCandidate"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-18))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-19)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-7-21)parser = JsonOutputToolsParser(return_id=True)

```


API Reference: [ChatPromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ChatPromptValue.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-8-1)initial_response = initial_answer_chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-8-2)  {"input": "Write a research report on lithium pollution."}
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-8-3))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-8-4)initial_response

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-9-1)AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_xRFx5hZJNyfurW9kWrPAWx15', 'function': {'arguments': '{"query":"lithium pollution research 2023"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 25, 'prompt_tokens': 93, 'total_tokens': 118, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a5d11b2ef2', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-448238e0-f2a7-4be0-b21d-03beb7d22121-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'lithium pollution research 2023'}, 'id': 'call_xRFx5hZJNyfurW9kWrPAWx15', 'type': 'tool_call'}], usage_metadata={'input_tokens': 93, 'output_tokens': 25, 'total_tokens': 118})

```


#### Starting Node[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#starting-node "Permanent link")

We will package up the candidate generation and reflection in a single node of our graph. This is represented by the following function:

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-1)# Define the node we will add to the graph
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-2)defgenerate_initial_response(state: TreeState) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-3)"""Generate the initial candidate response."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-4)  res = initial_answer_chain.invoke({"input": state["input"]})
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-5)  parsed = parser.invoke(res)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-6)  tool_responses = [
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-7)    tool_node.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-8)      {
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-9)        "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-10)          AIMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-11)            content="",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-12)            tool_calls=[
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-13)              {"name": r["type"], "args": r["args"], "id": r["id"]}
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-14)            ],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-15)          )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-16)        ]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-17)      }
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-18)    )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-19)    for r in parsed
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-20)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-21)  output_messages = [res] + [tr["messages"][0] for tr in tool_responses]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-22)  reflection = reflection_chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-23)    {"input": state["input"], "candidate": output_messages}
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-24)  )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-25)  root = Node(output_messages, reflection=reflection)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-26)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-27)    **state,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-28)    "root": root,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-10-29)  }

```


### Candidate Generation[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#candidate-generation "Permanent link")

The following code prompts the same LLM to generate N additional candidates to check.

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-1)# This generates N candidate values
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-2)# for a single input to sample actions from the environment
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-4)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-5)defgenerate_candidates(messages: ChatPromptValue, config: RunnableConfig):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-6)  n = config["configurable"].get("N", 5)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-7)  bound_kwargs = llm.bind_tools(tools=tools).kwargs
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-8)  chat_result = llm.generate(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-9)    [messages.to_messages()],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-10)    n=n,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-11)    callbacks=config["callbacks"],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-12)    run_name="GenerateCandidates",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-13)    **bound_kwargs,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-14)  )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-15)  return [gen.message for gen in chat_result.generations[0]]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-16)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-17)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-11-18)expansion_chain = prompt_template | generate_candidates

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-12-1)res = expansion_chain.invoke({"input": "Write a research report on lithium pollution."})
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-12-2)res

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-13-1)[AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'function': {'arguments': '{"query":"lithium pollution research 2023"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}], 'refusal': None}, response_metadata={'finish_reason': 'tool_calls', 'logprobs': None}, id='run-dc7c2f76-1eaf-4c65-8803-7ccededfcf0e-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'lithium pollution research 2023'}, 'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'type': 'tool_call'}], usage_metadata={'input_tokens': 93, 'output_tokens': 123, 'total_tokens': 216}),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-13-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'function': {'arguments': '{"query":"lithium pollution research report 2023"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}]}, response_metadata={'finish_reason': 'tool_calls', 'logprobs': None}, id='run-dc7c2f76-1eaf-4c65-8803-7ccededfcf0e-1', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'lithium pollution research report 2023'}, 'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'type': 'tool_call'}], usage_metadata={'input_tokens': 93, 'output_tokens': 123, 'total_tokens': 216}),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-13-3) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'function': {'arguments': '{"query":"lithium pollution research report"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}]}, response_metadata={'finish_reason': 'tool_calls', 'logprobs': None}, id='run-dc7c2f76-1eaf-4c65-8803-7ccededfcf0e-2', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'lithium pollution research report'}, 'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'type': 'tool_call'}], usage_metadata={'input_tokens': 93, 'output_tokens': 123, 'total_tokens': 216}),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-13-4) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'function': {'arguments': '{"query":"lithium pollution research report"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}]}, response_metadata={'finish_reason': 'tool_calls', 'logprobs': None}, id='run-dc7c2f76-1eaf-4c65-8803-7ccededfcf0e-3', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'lithium pollution research report'}, 'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'type': 'tool_call'}], usage_metadata={'input_tokens': 93, 'output_tokens': 123, 'total_tokens': 216}),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-13-5) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'function': {'arguments': '{"query":"lithium pollution research report 2023"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}]}, response_metadata={'finish_reason': 'tool_calls', 'logprobs': None}, id='run-dc7c2f76-1eaf-4c65-8803-7ccededfcf0e-4', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'lithium pollution research report 2023'}, 'id': 'call_rf2Ns2CW2LppxuUFI4irvRhM', 'type': 'tool_call'}], usage_metadata={'input_tokens': 93, 'output_tokens': 123, 'total_tokens': 216})]

```


#### Candidate generation node[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#candidate-generation-node "Permanent link")

We will package the candidate generation and reflection steps in the following "expand" node. We do all the operations as a batch process to speed up execution.

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-1)fromcollectionsimport defaultdict
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-4)defselect(root: Node) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-5)"""Starting from the root node a child node is selected at each tree level until a leaf node is reached."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-6)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-7)  if not root.children:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-8)    return root
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-9)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-10)  node = root
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-11)  while node.children:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-12)    max_child = max(node.children, key=lambda child: child.upper_confidence_bound())
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-13)    node = max_child
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-14)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-15)  return node
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-16)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-17)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-18)defexpand(state: TreeState, config: RunnableConfig) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-19)"""Starting from the "best" node in the tree, generate N candidates for the next step."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-20)  root = state["root"]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-21)  best_candidate: Node = select(root)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-22)  messages = best_candidate.get_trajectory()
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-23)  # Generate N candidates from the single child candidate
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-24)  new_candidates = expansion_chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-25)    {"input": state["input"], "messages": messages}, config
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-26)  )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-27)  parsed = parser.batch(new_candidates)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-28)  flattened = [
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-29)    (i, tool_call)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-30)    for i, tool_calls in enumerate(parsed)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-31)    for tool_call in tool_calls
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-32)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-33)  tool_responses = [
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-34)    (
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-35)      i,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-36)      tool_node.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-37)        {
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-38)          "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-39)            AIMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-40)              content="",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-41)              tool_calls=[
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-42)                {
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-43)                  "name": tool_call["type"],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-44)                  "args": tool_call["args"],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-45)                  "id": tool_call["id"],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-46)                }
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-47)              ],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-48)            )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-49)          ]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-50)        }
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-51)      ),
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-52)    )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-53)    for i, tool_call in flattened
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-54)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-55)  collected_responses = defaultdict(list)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-56)  for i, resp in tool_responses:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-57)    collected_responses[i].append(resp["messages"][0])
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-58)  output_messages = []
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-59)  for i, candidate in enumerate(new_candidates):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-60)    output_messages.append([candidate] + collected_responses[i])
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-61)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-62)  # Reflect on each candidate
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-63)  # For tasks with external validation, you'd add that here.
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-64)  reflections = reflection_chain.batch(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-65)    [{"input": state["input"], "candidate": msges} for msges in output_messages],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-66)    config,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-67)  )
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-68)  # Grow tree
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-69)  child_nodes = [
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-70)    Node(cand, parent=best_candidate, reflection=reflection)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-71)    for cand, reflection in zip(output_messages, reflections)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-72)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-73)  best_candidate.children.extend(child_nodes)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-74)  # We have already extended the tree directly, so we just return the state
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-14-75)  return state

```


## Create Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#create-graph "Permanent link")

With those two nodes defined, we are ready to define the graph. After each agent step, we have the option of finishing.

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-3)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-4)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-5)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-6)defshould_loop(state: TreeState):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-7)"""Determine whether to continue the tree search."""
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-8)  root = state["root"]
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-9)  if root.is_solved:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-10)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-11)  if root.height > 5:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-12)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-13)  return "expand"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-14)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-15)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-16)builder = StateGraph(TreeState)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-17)builder.add_node("start", generate_initial_response)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-18)builder.add_node("expand", expand)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-19)builder.add_edge(START, "start")
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-20)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-21)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-22)builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-23)  "start",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-24)  # Either expand/rollout or finish
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-25)  should_loop,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-26)  ["expand", END],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-27))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-28)builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-29)  "expand",
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-30)  # Either continue to rollout or finish
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-31)  should_loop,
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-32)  ["expand", END],
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-33))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-34)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-15-35)graph = builder.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-16-1)fromIPython.displayimport Image
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-16-3)Image(graph.get_graph().draw_mermaid_png())

```


![]()

## Invoke[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#invoke "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-17-1)question = "Generate a table with the average size and weight, as well as the oldest recorded instance for each of the top 5 most common birds."
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-17-2)last_step = None
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-17-3)for step in graph.stream({"input": question}):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-17-4)  last_step = step
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-17-5)  step_name, step_state = next(iter(step.items()))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-17-6)  print(step_name)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-17-7)  print("rolled out: ", step_state["root"].height)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-17-8)  print("---")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-18-1)start
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-18-2)rolled out: 1
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-18-3)---
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-18-4)expand
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-18-5)rolled out: 2
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-18-6)---

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-19-1)solution_node = last_step["expand"]["root"].get_best_solution()
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-19-2)best_trajectory = solution_node.get_trajectory(include_reflections=False)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-19-3)print(best_trajectory[-1].content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-1)Let's synthesize the information into a coherent table summarizing the average size, weight, and the oldest recorded instance for each of the top 5 most common birds.
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-2)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-3)### Top 5 Most Common Birds
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-4)Based on the search results, the top 5 most common birds are:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-5)1. Domestic Chicken
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-6)2. House Sparrow
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-7)3. European Starling
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-8)4. Ring-billed Gull
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-9)5. Barn Swallow
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-10)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-11)### Table: Average Size, Weight, and Oldest Recorded Instance
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-12)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-13)| Bird        | Average Size (cm) | Average Weight (g) | Oldest Recorded Instance |
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-14)|--------------------|-------------------|--------------------|-------------------------|
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-15)| Domestic Chicken  | 40-50       | 1,200-2,500    | ~16 years (Pet record) |
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-16)| House Sparrow   | 14-18       | 24-40       | 13 years        |
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-17)| European Starling | 20-23       | 58-100       | 15 years        |
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-18)| Ring-billed Gull  | 48-53       | 300-700      | 23 years        |
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-19)| Barn Swallow    | 15-20       | 17-20       | 16 years        |
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-20)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-21)### Additional Details
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-22)- **Domestic Chicken**: The average size and weight can vary significantly based on breed and diet. The oldest recorded pet chicken lived up to 16 years.
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-23)- **House Sparrow**: Commonly found in urban areas, with an average lifespan significantly shorter in the wild.
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-24)- **European Starling**: Known for their adaptability, starlings have a notable lifespan when not exposed to predators or harsh conditions.
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-25)- **Ring-billed Gull**: These gulls are common in North America and have a relatively long lifespan compared to other birds.
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-26)- **Barn Swallow**: Known for their migratory habits, these birds have relatively high longevity given their size.
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-27)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-20-28)This table now provides a structured and comprehensive summary of the requested information.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-21-1)question = "Write out magnus carlson series of moves in his game against Alireza Firouzja and propose an alternate strategy"
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-21-2)last_step = None
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-21-3)for step in graph.stream({"input": question}):
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-21-4)  last_step = step
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-21-5)  step_name, step_state = next(iter(step.items()))
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-21-6)  print(step_name)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-21-7)  print("rolled out: ", step_state["root"].height)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-21-8)  print("---")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-1)start
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-2)rolled out: 1
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-3)---
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-4)expand
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-5)rolled out: 2
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-6)---
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-7)expand
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-8)rolled out: 3
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-9)---
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-10)expand
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-11)rolled out: 3
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-12)---
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-13)expand
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-14)rolled out: 3
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-22-15)---

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-23-1)solution_node = last_step["expand"]["root"].get_best_solution()
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-23-2)best_trajectory = solution_node.get_trajectory(include_reflections=False)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-23-3)print(best_trajectory[-1].content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-1)It appears that the specific game moves between Magnus Carlsen and Alireza Firouzja are not readily available in the search results. However, I can provide a general idea of what a typical game between high-level players like Carlsen and Firouzja might look like and propose an alternate strategy based on common chess principles.
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-2)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-3)### Example Game Moves (Hypothetical)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-4)Here's a hypothetical sequence of moves in a game between Magnus Carlsen and Alireza Firouzja:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-5)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-6)1. e4 e5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-7)2. Nf3 Nc6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-8)3. Bb5 a6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-9)4. Ba4 Nf6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-10)5. O-O Be7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-11)6. Re1 b5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-12)7. Bb3 d6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-13)8. c3 O-O
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-14)9. h3 Nb8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-15)10. d4 Nbd7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-16)11. Nbd2 Bb7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-17)12. Bc2 Re8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-18)13. Nf1 Bf8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-19)14. Ng3 g6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-20)15. a4 c5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-21)16. d5 c4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-22)17. Be3 Qc7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-23)18. Qd2 Nc5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-24)19. Nh2 Bg7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-25)20. Ng4 Nxg4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-26)21. hxg4 Qd7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-27)22. f3 f6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-28)23. Kf2 Qf7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-29)24. Rh1 Rad8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-30)25. Rh3 Bc8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-31)26. Rah1 h6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-32)27. Bxh6 Bxh6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-33)28. Rxh6 Qg7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-34)29. g5 f5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-35)30. exf5 Bxf5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-36)31. Bxf5 gxf5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-37)32. Nh5 Qf7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-38)33. Nf6+ Kf8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-39)34. Rh8+ Ke7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-40)35. Rxe8+ Rxe8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-41)36. Nxe8 Qxe8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-42)37. Rh7+ Kd8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-43)38. g6 Qg8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-44)39. Qg5+ Kc8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-45)40. Qe7 Qd8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-46)41. Qxd8+ Kxd8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-47)42. g7 Kc7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-48)43. g8=Q+ Kb6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-49)44. Qb8+ Ka5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-50)45. Qd8+ Kxa4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-51)46. g4 fxg4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-52)47. fxg4 Kb3
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-53)48. g5 Kxb2
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-54)49. Qb6 Kxc3
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-55)50. Qxc5 dxc5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-56)51. d6 b4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-57)52. d7 b3
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-58)53. d8=Q b2
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-59)54. Qd1 b1=Q
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-60)55. Rxb1 Kxc4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-61)56. Qc1+ Kd5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-62)57. Qxc3 c4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-63)58. Ke3 Kc6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-64)59. Kd4 Kc7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-65)60. Qxc4+ Kd6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-66)61. Qc5+ Ke6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-67)62. Rb6+ Kf7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-68)63. Qc7+ Ke8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-69)64. Rb8#
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-70)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-71)### Alternate Strategy
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-72)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-73)If we consider that Magnus Carlsen played the white pieces and used a typical Ruy Lopez opening, an alternate strategy could involve a different opening or a variation within the Ruy Lopez itself. For instance:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-74)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-75)1. **Alternative Opening: The Italian Game**
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-76)  - 1. e4 e5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-77)  - 2. Nf3 Nc6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-78)  - 3. Bc4 Bc5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-79)  - 4. c3 Nf6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-80)  - 5. d4 exd4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-81)  - 6. cxd4 Bb4+
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-82)  - 7. Nc3 Nxe4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-83)  - 8. O-O Bxc3
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-84)  - 9. d5 Ne7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-85)  - 10. Qd3 f5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-86)  - 11. bxc3 d6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-87)  - 12. Nd4 O-O
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-88)  - 13. f3 Nc5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-89)  - 14. Qc2 f4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-90)  - 15. Re1 Ng6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-91)  - 16. Ba3 Qg5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-92)  - 17. Bxc5 dxc5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-93)  - 18. Ne6 Bxe6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-94)  - 19. dxe6 Ne7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-95)  - 20. Rad1 Rad8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-96)  - 21. Rd7 Rxd7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-97)  - 22. exd7+ Kh8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-98)  - 23. Qe4 Nc6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-99)  - 24. Bd3 g6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-100)  - 25. Qe8 Kg7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-101)  - 26. Bb5 Nd8
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-102)  - 27. Re7+ Kh6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-103)  - 28. Qxf8+ Kh5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-104)  - 29. Rxh7#
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-105)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-106)2. **Variation in the Ruy Lopez:**
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-107)  - Instead of the main lines, White could opt for the "Cozy Variation" or the "Deferred Steinitz Defense."
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-108)  - For example, after the initial moves:
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-109)   - 1. e4 e5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-110)   - 2. Nf3 Nc6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-111)   - 3. Bb5 a6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-112)   - 4. Ba4 d6 (Deferred Steinitz Defense)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-113)   - 5. c3 Bg4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-114)   - 6. h3 Bh5
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-115)   - 7. d4 exd4
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-116)   - 8. cxd4 Be7
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-117)   - 9. Nc3 Nf6
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-118)   - 10. O-O O-O
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-119)
[](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__codelineno-24-120)By varying the opening or the approach within a given opening, Carlsen could potentially avoid deep preparation by Firouzja and steer the game into less familiar territory for his opponent.

```


## Conclusion[¶](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#conclusion "Permanent link")

Congrats on implementing LATS! This is a technique that can be reasonably fast and effective at solving complex reasoning tasks. A few notes that you probably observed above: 1. While effective , the tree rollout can take additional compute time. If you wanted to include this in a production app, you'd either want to ensure that intermediate steps are streamed (so the user sees the thinking process/has access to intermediate results) or use it for fine-tuning data to improve the single-shot accuracy and avoid long rollouts. 2. The candidate selection process is only as good as the reward you generate. Here we are using self-reflection exclusively, but if you have an external source of feedback (such as code test execution), that should be incorporated in the locations mentioned above.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Tree of Thoughts  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/) [ Next  Self-Discover Agent  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
