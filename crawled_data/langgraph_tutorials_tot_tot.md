---
url: https://langchain-ai.github.io/langgraph/tutorials/tot/tot/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#tree-of-thoughts)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Tree of Thoughts 

[ ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/?q= "Share")

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
            * Tree of Thoughts  [ Tree of Thoughts  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/) Table of contents 
              * [ Prerequisites  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#prerequisites)
              * [ Task Definition  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#task-definition)
                * [ Fetch data  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#fetch-data)
              * [ Expander  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#expander)
            * [ Language Agent Tree Search  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/)
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

  * [ Prerequisites  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#prerequisites)
  * [ Task Definition  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#task-definition)
    * [ Fetch data  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#fetch-data)
  * [ Expander  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#expander)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
  5. [ Reflection & Critique  ](https://langchain-ai.github.io/langgraph/tutorials#reflection-critique)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/tot/tot.ipynb "Edit this page")

# Tree of Thoughts[¶](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#tree-of-thoughts "Permanent link")

[Tree of Thoughts](https://arxiv.org/abs/2305.10601) (ToT), by Yao, et. al, is a general LLM agent search algorithm that combines reflection/evaluation and simple search (in this case BFS, though you can apply DFS or other algorithms if you'd like).

![LATS diagram](https://langchain-ai.github.io/langgraph/tutorials/tot/img/tot.png)

It has three main steps:

  1. Expand: generate 1 or more candidate solutions to the problem.
  2. Score: measure the quality of the responses.
  3. Prune: retain the top K best candidates



Then return to "Expand" if no solution is found (or if the solution is of insufficient quality).

## Prerequisites[¶](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#prerequisites "Permanent link")

We'll install the tutorial's dependent packages and set our API key for the LLM provider of choice.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-0-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-10)_set_env("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-11)# To visualize the algorithm
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-12)trace = True
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-13)if trace:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-14)  _set_env("LANGSMITH_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-1-15)  os.environ["LANGSMITH_PROJECT"] = "ToT Tutorial"

```


## Task Definition[¶](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#task-definition "Permanent link")

Our agent will try to play the "Game of 24". Given 4 numbers, it must generate a math equation that uses each of these numbers exactly one time to evaluate to a value of `24`.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-1)importoperator
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-2)fromtypingimport List, Literal, Union, NamedTuple, Optional
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-3)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-5)OperatorType = Literal["+", "-", "*", "/"]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-6)TokenType = Union[float, OperatorType]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-8)## We use these schemas to prompt the LLM to generate equations that evaluate to 24.
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-11)classEquation(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-12)"""The formula combining the provided numbers to reach the target of 24."""
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-14)  tokens: List[TokenType] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-15)    description="The stack of tokens and operators in reverse-polish notation. Example: [3, 4, '+', -1, '*'] would evaluate to (3 + 4) * -1 = -7.",
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-16)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-18)  defcompute(self) -> float:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-19)    op_funcs = {
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-20)      "+": operator.add,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-21)      "-": operator.sub,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-22)      "*": operator.mul,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-23)      "/": operator.truediv,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-24)    }
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-25)    stack = []
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-26)    for token in self.tokens:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-27)      if isinstance(token, float):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-28)        stack.append(token)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-29)      else:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-30)        b, a = stack.pop(), stack.pop()
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-31)        stack.append(op_funcs[token](a, b))
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-32)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-33)    return stack[0]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-35)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-36)classGuessEquations(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-37)"""Submit multiple equations as guesses."""
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-38)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-39)  reasoning: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-40)    description="The reasoning behind the submitted guesses. Explain how you arrived at these equations."
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-41)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-42)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-43)  equations: List[Equation] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-44)    description="The list of equations to submit as guesses."
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-45)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-46)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-47)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-48)## These objects will represent a single "candidate" (or scored candidate) within our agent's state.
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-49)# You can update the candidate object to match your own task.
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-50)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-51)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-52)classCandidate(NamedTuple):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-53)  candidate: Equation
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-54)  score: Optional[float] = None
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-55)  feedback: Optional[str] = None
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-56)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-57)  def__str__(self):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-58)    try:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-59)      computed = self.candidate.compute()
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-60)    except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-61)      computed = f"Invalid equation: {self.candidate.tokens}; Error: {repr(e)}"
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-62)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-63)    return f"Equation({self.candidate.tokens}) = {computed} (Reward: {self.score})"
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-64)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-65)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-66)classScoredCandidate(Candidate):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-67)  candidate: Equation
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-68)  score: float
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-2-69)  feedback: str

```


#### Fetch data[¶](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#fetch-data "Permanent link")

We'll use an example from the [Game of 24](https://github.com/princeton-nlp/tree-of-thought-llm) dataset.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-1)importrequests
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-2)importcsv
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-4)csv_data = requests.get(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-5)  "https://storage.googleapis.com/benchmarks-artifacts/game-of-24/24.csv"
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-6)).content.decode("utf-8")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-7)# Get just the Puzzles column (column index 1)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-8)puzzles = [row[1].strip() for row in csv.reader(csv_data.splitlines()[1:])]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-3-10)print(f"Example puzzles: {puzzles[:3]}")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-4-1)Example puzzles: ['1 1 4 6', '1 1 11 11', '1 1 3 8']

```


## Expander[¶](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#expander "Permanent link")

The "tree of thoughts" algorithm is relatively generic. The primary two task-specific components are the **expander** and the **scorer**. The expander (the augmented LLM) tries to generate 1 or more solutions to the problem. On subsequent attempts, it is given a seed/candidate value from the previous search.

You can update this section to match your own task requirements. The expander can be arbitrarily complex. All that's required is that it accepts the problem and an optional previous attempt (or attempts) and returns a new result.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-1)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-5)prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-6)  [
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-7)    (
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-8)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-9)      "You are playing the Game of 24. Using the provide numbers, create an equation that evaluates to 24.\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-10)      "Submit exactly {k} guesses for this round.",
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-11)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-12)    ("user", "Solve the 24 game for these numbers: {problem}.{candidate}"),
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-13)  ],
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-14)).partial(candidate="")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-15)llm = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-17)bound_llm = llm.with_structured_output(GuessEquations)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-5-18)solver = prompt | bound_llm

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

# Scorer[¶](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#scorer "Permanent link")

In this game, the scorer is easy. We need to assert two things:

  1. The LLM has generated a valid equation using each number exactly one time.
  2. The equation evaluates to 24.



You can update this function to match your own task requirements.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-1)defcompute_score(problem: str, candidate: Candidate) -> ScoredCandidate:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-2)  numbers = list(map(int, problem.split()))
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-3)  # Check that the candidate equation uses all 4 numbers exactly once
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-4)  used_numbers = [
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-5)    token for token in candidate.candidate.tokens if isinstance(token, float)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-6)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-7)  if sorted(used_numbers) != sorted(numbers):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-8)    score = 0
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-9)    feedback = "The equation must use all 4 numbers exactly once."
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-10)    return ScoredCandidate(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-11)      candidate=candidate.candidate, score=score, feedback=feedback
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-12)    )
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-13)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-14)    result = candidate.candidate.compute()
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-15)    score = 1 / (1 + abs(24 - result))
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-16)    feedback = f"Result: {result}"
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-17)  except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-18)    score = 0
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-19)    feedback = f"Invalid equation. Error: {repr(e)}"
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-20)  return ScoredCandidate(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-21)    candidate=candidate.candidate, score=score, feedback=feedback
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-6-22)  )

```


## Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#graph "Permanent link")

Now it's time to create our graph.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-1)importoperator
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-2)fromtypingimport Optional, Dict, Any
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-3)fromtyping_extensionsimport Annotated, TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-4)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-6)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-7)fromlanggraph.constantsimport Send
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-8)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-11)defupdate_candidates(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-12)  existing: Optional[list] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-13)  updates: Optional[Union[list, Literal["clear"]]] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-14)) -> List[str]:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-15)  if existing is None:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-16)    existing = []
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-17)  if updates is None:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-18)    return existing
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-19)  if updates == "clear":
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-20)    return []
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-21)  # Concatenate the lists
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-22)  return existing + updates
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-23)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-24)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-25)classToTState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-26)  problem: str
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-27)  candidates: Annotated[List[Candidate], update_candidates]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-28)  scored_candidates: Annotated[List[ScoredCandidate], update_candidates]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-29)  depth: Annotated[int, operator.add]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-30)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-31)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-32)classConfiguration(TypedDict, total=False):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-33)  max_depth: int
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-34)  threshold: float
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-35)  k: int
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-36)  beam_size: int
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-37)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-38)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-39)def_ensure_configurable(config: RunnableConfig) -> Configuration:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-40)"""Get params that configure the search algorithm."""
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-41)  configurable = config.get("configurable", {})
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-42)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-43)    **configurable,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-44)    "max_depth": configurable.get("max_depth", 10),
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-45)    "threshold": config.get("threshold", 0.9),
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-46)    "k": configurable.get("k", 5),
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-47)    "beam_size": configurable.get("beam_size", 3),
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-48)  }
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-49)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-50)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-51)classExpansionState(ToTState):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-52)  seed: Optional[Candidate]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-53)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-54)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-55)defexpand(state: ExpansionState, *, config: RunnableConfig) -> Dict[str, List[str]]:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-56)"""Generate the next state."""
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-57)  configurable = _ensure_configurable(config)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-58)  if not state.get("seed"):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-59)    candidate_str = ""
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-60)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-61)    candidate_str = "\n\n" + str(state["seed"])
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-62)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-63)    equation_submission = solver.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-64)      {
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-65)        "problem": state["problem"],
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-66)        "candidate": candidate_str,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-67)        "k": configurable["k"],
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-68)      },
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-69)      config=config,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-70)    )
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-71)  except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-72)    return {"candidates": []}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-73)  new_candidates = [
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-74)    Candidate(candidate=equation) for equation in equation_submission.equations
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-75)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-76)  return {"candidates": new_candidates}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-77)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-78)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-79)defscore(state: ToTState) -> Dict[str, List[float]]:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-80)"""Evaluate the candidate generations."""
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-81)  candidates = state["candidates"]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-82)  scored = []
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-83)  for candidate in candidates:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-84)    scored.append(compute_score(state["problem"], candidate))
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-85)  return {"scored_candidates": scored, "candidates": "clear"}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-86)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-87)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-88)defprune(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-89)  state: ToTState, *, config: RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-90)) -> Dict[str, List[Dict[str, Any]]]:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-91)  scored_candidates = state["scored_candidates"]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-92)  beam_size = _ensure_configurable(config)["beam_size"]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-93)  organized = sorted(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-94)    scored_candidates, key=lambda candidate: candidate[1], reverse=True
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-95)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-96)  pruned = organized[:beam_size]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-97)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-98)    # Update the starting point for the next iteration
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-99)    "candidates": pruned,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-100)    # Clear the old memory
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-101)    "scored_candidates": "clear",
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-102)    # Increment the depth by 1
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-103)    "depth": 1,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-104)  }
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-105)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-106)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-107)defshould_terminate(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-108)  state: ToTState, config: RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-109)) -> Union[Literal["__end__"], Send]:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-110)  configurable = _ensure_configurable(config)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-111)  solved = state["candidates"][0].score >= configurable["threshold"]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-112)  if solved or state["depth"] >= configurable["max_depth"]:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-113)    return "__end__"
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-114)  return [
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-115)    Send("expand", {**state, "somevalseed": candidate})
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-116)    for candidate in state["candidates"]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-117)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-118)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-119)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-120)# Create the graph
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-121)builder = StateGraph(state_schema=ToTState, config_schema=Configuration)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-122)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-123)# Add nodes
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-124)builder.add_node(expand)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-125)builder.add_node(score)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-126)builder.add_node(prune)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-127)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-128)# Add edges
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-129)builder.add_edge("expand", "score")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-130)builder.add_edge("score", "prune")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-131)builder.add_conditional_edges("prune", should_terminate, path_map=["expand", "__end__"])
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-132)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-133)# Set entry point
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-134)builder.add_edge("__start__", "expand")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-135)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-136)# Compile the graph
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-7-137)graph = builder.compile(checkpointer=MemorySaver())

```


API Reference: [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [Send](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-8-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-8-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

## Run[¶](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#run "Permanent link")

Now let's try it on one of the puzzles!

```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-9-1)config = {
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-9-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-9-3)    "thread_id": "test_1",
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-9-4)    "depth": 10,
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-9-5)  }
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-9-6)}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-9-7)for step in graph.stream({"problem": puzzles[42]}, config):
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-9-8)  print(step)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-10-1){'expand': {'candidates': [Candidate(candidate=Equation(tokens=[12.0, 5.0, '/', 7.0, '*']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[12.0, 1.0, '+', 5.0, '*']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[12.0, 7.0, '*', 1.0, '/']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[5.0, 7.0, '*', 1.0, '*']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[7.0, 5.0, '*', 12.0, '/']), score=None, feedback=None)]}}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-10-2){'score': {'candidates': 'clear', 'scored_candidates': [ScoredCandidate(candidate=Equation(tokens=[12.0, 5.0, '/', 7.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[12.0, 1.0, '+', 5.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[12.0, 7.0, '*', 1.0, '/']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[5.0, 7.0, '*', 1.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[7.0, 5.0, '*', 12.0, '/']), score=0, feedback='The equation must use all 4 numbers exactly once.')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-10-3){'prune': {'candidates': [ScoredCandidate(candidate=Equation(tokens=[12.0, 5.0, '/', 7.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[12.0, 1.0, '+', 5.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[12.0, 7.0, '*', 1.0, '/']), score=0, feedback='The equation must use all 4 numbers exactly once.')], 'scored_candidates': 'clear', 'depth': 1}}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-10-4){'expand': {'candidates': [Candidate(candidate=Equation(tokens=[12.0, 5.0, '-', 1.0, '*']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[1.0, 7.0, '*', 5.0, '+']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[12.0, 1.0, '+', 5.0, '*']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[7.0, 5.0, '*', 1.0, '-']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[12.0, 1.0, '*', 5.0, '-']), score=None, feedback=None)]}}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-10-5){'expand': {'candidates': []}}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-10-6){'expand': {'candidates': [Candidate(candidate=Equation(tokens=[5.0, 7.0, '*', 12.0, '-']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[1.0, 5.0, 7.0, '*', 12.0, '-', '+']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[12.0, 1.0, '*', 5.0, 7.0, '/']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[12.0, 5.0, '*', 7.0, '/', 1.0, '-']), score=None, feedback=None), Candidate(candidate=Equation(tokens=[5.0, 7.0, '*', 1.0, '-', 12.0, '+']), score=None, feedback=None)]}}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-10-7){'score': {'candidates': 'clear', 'scored_candidates': [ScoredCandidate(candidate=Equation(tokens=[12.0, 5.0, '/', 7.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[12.0, 1.0, '+', 5.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[12.0, 7.0, '*', 1.0, '/']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[5.0, 7.0, '*', 12.0, '-']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[1.0, 5.0, 7.0, '*', 12.0, '-', '+']), score=1.0, feedback='Result: 24.0'), ScoredCandidate(candidate=Equation(tokens=[12.0, 1.0, '*', 5.0, 7.0, '/']), score=0.07692307692307693, feedback='Result: 12.0'), ScoredCandidate(candidate=Equation(tokens=[12.0, 5.0, '*', 7.0, '/', 1.0, '-']), score=0.05737704918032786, feedback='Result: 7.571428571428571'), ScoredCandidate(candidate=Equation(tokens=[5.0, 7.0, '*', 1.0, '-', 12.0, '+']), score=0.043478260869565216, feedback='Result: 46.0'), ScoredCandidate(candidate=Equation(tokens=[12.0, 5.0, '-', 1.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[1.0, 7.0, '*', 5.0, '+']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[12.0, 1.0, '+', 5.0, '*']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[7.0, 5.0, '*', 1.0, '-']), score=0, feedback='The equation must use all 4 numbers exactly once.'), ScoredCandidate(candidate=Equation(tokens=[12.0, 1.0, '*', 5.0, '-']), score=0, feedback='The equation must use all 4 numbers exactly once.')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-10-8){'prune': {'candidates': [ScoredCandidate(candidate=Equation(tokens=[1.0, 5.0, 7.0, '*', 12.0, '-', '+']), score=1.0, feedback='Result: 24.0'), ScoredCandidate(candidate=Equation(tokens=[12.0, 1.0, '*', 5.0, 7.0, '/']), score=0.07692307692307693, feedback='Result: 12.0'), ScoredCandidate(candidate=Equation(tokens=[12.0, 5.0, '*', 7.0, '/', 1.0, '-']), score=0.05737704918032786, feedback='Result: 7.571428571428571')], 'scored_candidates': 'clear', 'depth': 1}}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-1)final_state = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-2)winning_solution = final_state.values["candidates"][0]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-3)search_depth = final_state.values["depth"]
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-4)if winning_solution[1] == 1:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-5)  print(f"Found a winning solution in {search_depth} steps: {winning_solution}")
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-6)else:
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-7)  print(
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-8)    f"Failed to find a winning solution in {search_depth} steps. Best guess: {winning_solution}"
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-11-9)  )

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__codelineno-12-1)Found a winning solution in 2 steps: [Equation(tokens=[1.0, 5.0, 7.0, '*', 12.0, '-', '+']), 1.0, 'Result: 24.0']

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Reflexion  ](https://langchain-ai.github.io/langgraph/tutorials/reflexion/reflexion/) [ Next  Language Agent Tree Search  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
