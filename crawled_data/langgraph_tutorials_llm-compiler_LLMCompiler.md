---
url: https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#llmcompiler)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

LLMCompiler 

[ ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/?q= "Share")

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
          * Planning Agents  Planning Agents 
            * [ Planning Agents  ](https://langchain-ai.github.io/langgraph/tutorials#planning-agents)
            * [ Plan-and-Execute  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/)
            * [ Reasoning without Observation  ](https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/)
            * LLMCompiler  [ LLMCompiler  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#setup)
              * [ Helper Files  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#helper-files)
                * [ Math Tools  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#math-tools)
                * [ Output Parser  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#output-parser)
              * [ Define Tools  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#define-tools)
              * [ Planner  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#planner)
              * [ Task Fetching Unit  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#task-fetching-unit)
                * [ Example Plan  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#example-plan)
              * [ Joiner  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#joiner)
              * [ Compose using LangGraph  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#compose-using-langgraph)
                * [ Simple question  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#simple-question)
                * [ Multi-hop question  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#multi-hop-question)
                * [ Multi-step math  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#multi-step-math)
                * [ Complex Replanning Example  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#complex-replanning-example)
              * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#conclusion)
          * [ Reflection & Critique  ](https://langchain-ai.github.io/langgraph/tutorials#reflection-critique)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#setup)
  * [ Helper Files  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#helper-files)
    * [ Math Tools  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#math-tools)
    * [ Output Parser  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#output-parser)
  * [ Define Tools  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#define-tools)
  * [ Planner  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#planner)
  * [ Task Fetching Unit  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#task-fetching-unit)
    * [ Example Plan  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#example-plan)
  * [ Joiner  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#joiner)
  * [ Compose using LangGraph  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#compose-using-langgraph)
    * [ Simple question  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#simple-question)
    * [ Multi-hop question  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#multi-hop-question)
    * [ Multi-step math  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#multi-step-math)
    * [ Complex Replanning Example  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#complex-replanning-example)
  * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#conclusion)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
  5. [ Planning Agents  ](https://langchain-ai.github.io/langgraph/tutorials#planning-agents)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/llm-compiler/LLMCompiler.ipynb "Edit this page")

# LLMCompiler[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#llmcompiler "Permanent link")

This notebook shows how to implement [LLMCompiler, by Kim, et. al](https://arxiv.org/abs/2312.04511) in LangGraph.

LLMCompiler is an agent architecture designed to **speed up** the execution of agentic tasks by eagerly-executed tasks within a DAG. It also saves costs on redundant token usage by reducing the number of calls to the LLM. Below is an overview of its computational graph:

![LLMCompiler Graph]()

It has 3 main components:

  1. Planner: stream a DAG of tasks.
  2. Task Fetching Unit: schedules and executes the tasks as soon as they are executable
  3. Joiner: Responds to the user or triggers a second plan



This notebook walks through each component and shows how to wire them together using LangGraph. The end result will leave a trace [like the following](https://smith.langchain.com/public/218c2677-c719-4147-b0e9-7bc3b5bb2623/r).

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-0-2)%pip install -U --quiet langchain_openai langsmith langgraph langchain numexpr

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-5)def_get_pass(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-6)  if var not in os.environ:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-1-10)_get_pass("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Helper Files[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#helper-files "Permanent link")

### Math Tools[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#math-tools "Permanent link")

Place the following code in a file called `math_tools.py` and ensure that you can import it into this notebook.

Show/Hide Math Tools

```

  import math
  import re
  from typing import List, Optional
  import numexpr
  from langchain.chains.openai_functions import create_structured_output_runnable
  from langchain_core.messages import SystemMessage
  from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
  from langchain_core.runnables import RunnableConfig
  from langchain_core.tools import StructuredTool
  from langchain_openai import ChatOpenAI
  from pydantic import BaseModel, Field
  _MATH_DESCRIPTION = (
    "math(problem: str, context: Optional[list[str]]) -> float:\n"
    " - Solves the provided math problem.\n"
    ' - `problem` can be either a simple math problem (e.g. "1 + 3") or a word problem (e.g. "how many apples are there if there are 3 apples and 2 apples").\n'
    " - You cannot calculate multiple expressions in one call. For instance, `math('1 + 3, 2 + 4')` does not work. "
    "If you need to calculate multiple expressions, you need to call them separately like `math('1 + 3')` and then `math('2 + 4')`\n"
    " - Minimize the number of `math` actions as much as possible. For instance, instead of calling "
    '2. math("what is the 10% of $1") and then call 3. math("$1 + $2"), '
    'you MUST call 2. math("what is the 110% of $1") instead, which will reduce the number of math actions.\n'
    # Context specific rules below
    " - You can optionally provide a list of strings as `context` to help the agent solve the problem. "
    "If there are multiple contexts you need to answer the question, you can provide them as a list of strings.\n"
    " - `math` action will not see the output of the previous actions unless you provide it as `context`. "
    "You MUST provide the output of the previous actions as `context` if you need to do math on it.\n"
    " - You MUST NEVER provide `search` type action's outputs as a variable in the `problem` argument. "
    "This is because `search` returns a text blob that contains the information about the entity, not a number or value. "
    "Therefore, when you need to provide an output of `search` action, you MUST provide it as a `context` argument to `math` action. "
    'For example, 1. search("Barack Obama") and then 2. math("age of $1") is NEVER allowed. '
    'Use 2. math("age of Barack Obama", context=["$1"]) instead.\n'
    " - When you ask a question about `context`, specify the units. "
    'For instance, "what is xx in height?" or "what is xx in millions?" instead of "what is xx?"\n'
  )

  _SYSTEM_PROMPT = """Translate a math problem into a expression that can be executed using Python's numexpr library. Use the output of running this code to answer the question.
  Question: ${{Question with math problem.}}
  

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-2-1)${{single line mathematical expression that solves the problem}}

```


...numexpr.evaluate(text)... 

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-3-1)${{Output of running the code}}

```


Answer: ${{Answer}} Begin. Question: What is 37593 * 67? ExecuteCode({{code: "37593 * 67"}}) ...numexpr.evaluate("37593 * 67")... 

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-4-1)2518731

```


Answer: 2518731 Question: 37593^(1/5) ExecuteCode({{code: "37593**(1/5)"}}) ...numexpr.evaluate("37593**(1/5)")... 

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-5-1)8.222831614237718

```


Answer: 8.222831614237718 """ _ADDITIONAL_CONTEXT_PROMPT = """The following additional context is provided from other functions.\ Use it to substitute into any ${{#}} variables or other words in the problem.\ \n\n${context}\n\nNote that context variables are not defined in code yet.\ You must extract the relevant numbers and directly put them in code.""" class ExecuteCode(BaseModel): """The input to the numexpr.evaluate() function.""" reasoning: str = Field( ..., description="The reasoning behind the code expression, including how context is included, if applicable.", ) code: str = Field( ..., description="The simple code expression to execute by numexpr.evaluate().", ) def _evaluate_expression(expression: str) -> str: try: local_dict = {"pi": math.pi, "e": math.e} output = str( numexpr.evaluate( expression.strip(), global_dict={}, # restrict access to globals local_dict=local_dict, # add common mathematical functions ) ) except Exception as e: raise ValueError( f'Failed to evaluate "{expression}". Raised error: {repr(e)}.' " Please try again with a valid numerical expression" ) # Remove any leading and trailing brackets from the output return re.sub(r"^\\[|\\]$", "", output) def get_math_tool(llm: ChatOpenAI): prompt = ChatPromptTemplate.from_messages( [ ("system", _SYSTEM_PROMPT), ("user", "{problem}"), MessagesPlaceholder(variable_name="context", optional=True), ] ) extractor = prompt | llm.with_structured_output(ExecuteCode) def calculate_expression( problem: str, context: Optional[List[str]] = None, config: Optional[RunnableConfig] = None, ): chain_input = {"problem": problem} if context: context_str = "\n".join(context) if context_str.strip(): context_str = _ADDITIONAL_CONTEXT_PROMPT.format( context=context_str.strip() ) chain_input["context"] = [SystemMessage(content=context_str)] code_model = extractor.invoke(chain_input, config) try: return _evaluate_expression(code_model.code) except Exception as e: return repr(e) return StructuredTool.from_function( name="math", func=calculate_expression, description=_MATH_DESCRIPTION, ) 
```


### Output Parser[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#output-parser "Permanent link")

Show/Hide Output Parser

```

  import ast
  import re
  from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
  )
  from langchain_core.exceptions import OutputParserException
  from langchain_core.messages import BaseMessage
  from langchain_core.output_parsers.transform import BaseTransformOutputParser
  from langchain_core.runnables import RunnableConfig
  from langchain_core.tools import BaseTool
  from typing_extensions import TypedDict
  THOUGHT_PATTERN = r"Thought: ([^\n]*)"
  ACTION_PATTERN = r"\n*(\d+)\. (\w+)\((.*)\)(\s*#\w+\n)?"
  # $1 or ${1} -> 1
  ID_PATTERN = r"\$\{?(\d+)\}?"
  END_OF_PLAN = ""

  ### Helper functions

  def _ast_parse(arg: str) -> Any:
    try:
      return ast.literal_eval(arg)
    except: # noqa
      return arg

  def _parse_llm_compiler_action_args(args: str, tool: Union[str, BaseTool]) -> list[Any]:
    """Parse arguments from a string."""
    if args == "":
      return ()
    if isinstance(tool, str):
      return ()
    extracted_args = {}
    tool_key = None
    prev_idx = None
    for key in tool.args.keys():
      # Split if present
      if f"{key}=" in args:
        idx = args.index(f"{key}=")
        if prev_idx is not None:
          extracted_args[tool_key] = _ast_parse(
            args[prev_idx:idx].strip().rstrip(",")
          )
        args = args.split(f"{key}=", 1)[1]
        tool_key = key
        prev_idx = 0
    if prev_idx is not None:
      extracted_args[tool_key] = _ast_parse(
        args[prev_idx:].strip().rstrip(",").rstrip(")")
      )
    return extracted_args

  def default_dependency_rule(idx, args: str):
    matches = re.findall(ID_PATTERN, args)
    numbers = [int(match) for match in matches]
    return idx in numbers

  def _get_dependencies_from_graph(
    idx: int, tool_name: str, args: Dict[str, Any]
  ) -> dict[str, list[str]]:
    """Get dependencies from a graph."""
    if tool_name == "join":
      return list(range(1, idx))
    return [i for i in range(1, idx) if default_dependency_rule(i, str(args))]

  class Task(TypedDict):
    idx: int
    tool: BaseTool
    args: list
    dependencies: Dict[str, list]
    thought: Optional[str]

  def instantiate_task(
    tools: Sequence[BaseTool],
    idx: int,
    tool_name: str,
    args: Union[str, Any],
    thought: Optional[str] = None,
  ) -> Task:
    if tool_name == "join":
      tool = "join"
    else:
      try:
        tool = tools[[tool.name for tool in tools].index(tool_name)]
      except ValueError as e:
        raise OutputParserException(f"Tool {tool_name} not found.") from e
    tool_args = _parse_llm_compiler_action_args(args, tool)
    dependencies = _get_dependencies_from_graph(idx, tool_name, tool_args)
    return Task(
      idx=idx,
      tool=tool,
      args=tool_args,
      dependencies=dependencies,
      thought=thought,
    )

  class LLMCompilerPlanParser(BaseTransformOutputParser[dict], extra="allow"):
    """Planning output parser."""
    tools: List[BaseTool]
    def _transform(self, input: Iterator[Union[str, BaseMessage]]) -> Iterator[Task]:
      texts = []
      # TODO: Cleanup tuple state tracking here.
      thought = None
      for chunk in input:
        # Assume input is str. TODO: support vision/other formats
        text = chunk if isinstance(chunk, str) else str(chunk.content)
        for task, thought in self.ingest_token(text, texts, thought):
          yield task
      # Final possible task
      if texts:
        task, _ = self._parse_task("".join(texts), thought)
        if task:
          yield task
    def parse(self, text: str) -> List[Task]:
      return list(self._transform([text]))
    def stream(
      self,
      input: str | BaseMessage,
      config: RunnableConfig | None = None,
      **kwargs: Any | None,
    ) -> Iterator[Task]:
      yield from self.transform([input], config, **kwargs)
    def ingest_token(
      self, token: str, buffer: List[str], thought: Optional[str]
    ) -> Iterator[Tuple[Optional[Task], str]]:
      buffer.append(token)
      if "\n" in token:
        buffer_ = "".join(buffer).split("\n")
        suffix = buffer_[-1]
        for line in buffer_[:-1]:
          task, thought = self._parse_task(line, thought)
          if task:
            yield task, thought
        buffer.clear()
        buffer.append(suffix)
    def _parse_task(self, line: str, thought: Optional[str] = None):
      task = None
      if match := re.match(THOUGHT_PATTERN, line):
        # Optionally, action can be preceded by a thought
        thought = match.group(1)
      elif match := re.match(ACTION_PATTERN, line):
        # if action is parsed, return the task, and clear the buffer
        idx, tool_name, args, _ = match.groups()
        idx = int(idx)
        task = instantiate_task(
          tools=self.tools,
          idx=idx,
          tool_name=tool_name,
          args=args,
          thought=thought,
        )
        thought = None
      # Else it is just dropped
      return task, thought


```


## Define Tools[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#define-tools "Permanent link")

We'll first define the tools for the agent to use in our demo. We'll give it the class search engine + calculator combo.

If you don't want to sign up for tavily, you can replace it with the free [DuckDuckGo](https://python.langchain.com/docs/integrations/tools/ddg/).

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-1)fromlangchain_community.tools.tavily_searchimport TavilySearchResults
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-3)frommath_toolsimport get_math_tool
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-5)_get_pass("TAVILY_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-7)calculate = get_math_tool(ChatOpenAI(model="gpt-4-turbo-preview"))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-8)search = TavilySearchResults(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-9)  max_results=1,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-10)  description='tavily_search_results_json(query="the search query") - a search engine.',
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-11))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-6-13)tools = [search, calculate]

```


API Reference: [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-7-1)calculate.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-7-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-7-3)    "problem": "What's the temp of sf + 5?",
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-7-4)    "context": ["Thet empreature of sf is 32 degrees"],
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-7-5)  }
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-7-6))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-8-1)'37'

```


## Planner[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#planner "Permanent link")

Largely adapted from [the original source code](https://github.com/SqueezeAILab/LLMCompiler/blob/main/src/llm_compiler/output_parser.py), the planner accepts the input question and generates a task list to execute.

If it is provided with a previous plan, it is instructed to re-plan, which is useful if, upon completion of the first batch of tasks, the agent must take more actions.

The code below composes constructs the prompt template for the planner and composes it with LLM and output parser, defined in `output_parser.py`. The output parser processes a task list in the following form:

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-9-1)1. tool_1(arg1="arg1", arg2=3.5, ...)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-9-2)Thought: I then want to find out Y by using tool_2
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-9-3)2. tool_2(arg1="", arg2="${1}")'
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-9-4)3. join()<END_OF_PLAN>"

```


The "Thought" lines are optional. The `${#}` placeholders are variables. These are used to route tool (task) outputs to other tools.

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-1)fromtypingimport Sequence
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-3)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-4)fromlangchain_core.language_modelsimport BaseChatModel
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-5)fromlangchain_core.messagesimport (
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-6)  BaseMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-7)  FunctionMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-8)  HumanMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-9)  SystemMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-10))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-11)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-12)fromlangchain_core.runnablesimport RunnableBranch
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-13)fromlangchain_core.toolsimport BaseTool
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-14)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-15)fromoutput_parserimport LLMCompilerPlanParser, Task
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-16)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-17)prompt = hub.pull("wfh/llm-compiler")
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-10-18)print(prompt.pretty_print())

```


API Reference: [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [RunnableBranch](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.branch.RunnableBranch.html) | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-1)================================[1m System Message [0m================================
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-3)Given a user query, create a plan to solve it with the utmost parallelizability. Each plan should comprise an action from the following [33;1m[1;3m{num_tools}[0m types:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-4)[33;1m[1;3m{tool_descriptions}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-5)[33;1m[1;3m{num_tools}[0m. join(): Collects and combines results from prior actions.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-7) - An LLM agent is called upon invoking join() to either finalize the user query or wait until the plans are executed.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-8) - join should always be the last action in the plan, and will be called in two scenarios:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-9)  (a) if the answer can be determined by gathering the outputs from tasks to generate the final response.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-10)  (b) if the answer cannot be determined in the planning phase before you execute the plans. Guidelines:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-11) - Each action described above contains input/output types and description.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-12)  - You must strictly adhere to the input and output types for each action.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-13)  - The action descriptions contain the guidelines. You MUST strictly follow those guidelines when you use the actions.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-14) - Each action in the plan should strictly be one of the above types. Follow the Python conventions for each action.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-15) - Each action MUST have a unique ID, which is strictly increasing.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-16) - Inputs for actions can either be constants or outputs from preceding actions. In the latter case, use the format $id to denote the ID of the previous action whose output will be the input.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-17) - Always call join as the last action in the plan. Say '<END_OF_PLAN>' after you call join
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-18) - Ensure the plan maximizes parallelizability.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-19) - Only use the provided action types. If a query cannot be addressed using these, invoke the join action for the next steps.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-20) - Never introduce new actions other than the ones provided.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-21)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-22)=============================[1m Messages Placeholder [0m=============================
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-23)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-24)[33;1m[1;3m{messages}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-25)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-26)================================[1m System Message [0m================================
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-27)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-28)Remember, ONLY respond with the task list in the correct format! E.g.:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-29)idx. tool(arg_name=args)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-11-30)None

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-1)defcreate_planner(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-2)  llm: BaseChatModel, tools: Sequence[BaseTool], base_prompt: ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-3)):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-4)  tool_descriptions = "\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-5)    f"{i+1}. {tool.description}\n"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-6)    for i, tool in enumerate(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-7)      tools
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-8)    ) # +1 to offset the 0 starting index, we want it count normally from 1.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-9)  )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-10)  planner_prompt = base_prompt.partial(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-11)    replan="",
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-12)    num_tools=len(tools)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-13)    + 1, # Add one because we're adding the join() tool at the end.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-14)    tool_descriptions=tool_descriptions,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-15)  )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-16)  replanner_prompt = base_prompt.partial(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-17)    replan=' - You are given "Previous Plan" which is the plan that the previous agent created along with the execution results '
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-18)    "(given as Observation) of each plan and a general thought (given as Thought) about the executed results."
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-19)    'You MUST use these information to create the next plan under "Current Plan".\n'
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-20)    ' - When starting the Current Plan, you should start with "Thought" that outlines the strategy for the next plan.\n'
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-21)    " - In the Current Plan, you should NEVER repeat the actions that are already executed in the Previous Plan.\n"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-22)    " - You must continue the task index from the end of the previous one. Do not repeat task indices.",
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-23)    num_tools=len(tools) + 1,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-24)    tool_descriptions=tool_descriptions,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-25)  )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-26)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-27)  defshould_replan(state: list):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-28)    # Context is passed as a system message
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-29)    return isinstance(state[-1], SystemMessage)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-30)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-31)  defwrap_messages(state: list):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-32)    return {"messages": state}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-33)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-34)  defwrap_and_get_last_index(state: list):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-35)    next_task = 0
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-36)    for message in state[::-1]:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-37)      if isinstance(message, FunctionMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-38)        next_task = message.additional_kwargs["idx"] + 1
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-39)        break
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-40)    state[-1].content = state[-1].content + f" - Begin counting at : {next_task}"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-41)    return {"messages": state}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-42)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-43)  return (
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-44)    RunnableBranch(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-45)      (should_replan, wrap_and_get_last_index | replanner_prompt),
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-46)      wrap_messages | planner_prompt,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-47)    )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-48)    | llm
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-49)    | LLMCompilerPlanParser(tools=tools)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-12-50)  )

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-13-1)llm = ChatOpenAI(model="gpt-4-turbo-preview")
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-13-2)# This is the primary "agent" in our application
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-13-3)planner = create_planner(llm, tools, prompt)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-14-1)example_question = "What's the temperature in SF raised to the 3rd power?"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-14-3)for task in planner.stream([HumanMessage(content=example_question)]):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-14-4)  print(task["tool"], task["args"])
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-14-5)  print("---")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-15-1)description='tavily_search_results_json(query="the search query") - a search engine.' max_results=1 api_wrapper=TavilySearchAPIWrapper(tavily_api_key=SecretStr('**********')) {'query': 'current temperature in San Francisco'}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-15-2)---
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-15-3)name='math' description='math(problem: str, context: Optional[list[str]]) -> float:\n - Solves the provided math problem.\n - `problem` can be either a simple math problem (e.g. "1 + 3") or a word problem (e.g. "how many apples are there if there are 3 apples and 2 apples").\n - You cannot calculate multiple expressions in one call. For instance, `math(\'1 + 3, 2 + 4\')` does not work. If you need to calculate multiple expressions, you need to call them separately like `math(\'1 + 3\')` and then `math(\'2 + 4\')`\n - Minimize the number of `math` actions as much as possible. For instance, instead of calling 2. math("what is the 10% of $1") and then call 3. math("$1 + $2"), you MUST call 2. math("what is the 110% of $1") instead, which will reduce the number of math actions.\n - You can optionally provide a list of strings as `context` to help the agent solve the problem. If there are multiple contexts you need to answer the question, you can provide them as a list of strings.\n - `math` action will not see the output of the previous actions unless you provide it as `context`. You MUST provide the output of the previous actions as `context` if you need to do math on it.\n - You MUST NEVER provide `search` type action\'s outputs as a variable in the `problem` argument. This is because `search` returns a text blob that contains the information about the entity, not a number or value. Therefore, when you need to provide an output of `search` action, you MUST provide it as a `context` argument to `math` action. For example, 1. search("Barack Obama") and then 2. math("age of $1") is NEVER allowed. Use 2. math("age of Barack Obama", context=["$1"]) instead.\n - When you ask a question about `context`, specify the units. For instance, "what is xx in height?" or "what is xx in millions?" instead of "what is xx?"' args_schema=<class 'langchain_core.utils.pydantic.math'> func=<function get_math_tool.<locals>.calculate_expression at 0x11bed0fe0> {'problem': 'x ** 3', 'context': ['$1']}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-15-4)---
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-15-5)join ()
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-15-6)---

```


## Task Fetching Unit[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#task-fetching-unit "Permanent link")

This component schedules the tasks. It receives a stream of tools of the following format:

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-16-1){
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-16-2)tool:BaseTool,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-16-3)dependencies:number[],
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-16-4)}

```


The basic idea is to begin executing tools as soon as their dependencies are met. This is done through multi-threading. We will combine the task fetching unit and executor below:

![diagram]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-1)importre
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-2)importtime
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-3)fromconcurrent.futuresimport ThreadPoolExecutor, wait
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-4)fromtypingimport Any, Dict, Iterable, List, Union
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-6)fromlangchain_core.runnablesimport (
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-7)  chain as as_runnable,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-8))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-9)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-10)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-11)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-12)def_get_observations(messages: List[BaseMessage]) -> Dict[int, Any]:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-13)  # Get all previous tool responses
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-14)  results = {}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-15)  for message in messages[::-1]:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-16)    if isinstance(message, FunctionMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-17)      results[int(message.additional_kwargs["idx"])] = message.content
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-18)  return results
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-19)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-20)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-21)classSchedulerInput(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-22)  messages: List[BaseMessage]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-23)  tasks: Iterable[Task]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-24)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-25)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-26)def_execute_task(task, observations, config):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-27)  tool_to_use = task["tool"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-28)  if isinstance(tool_to_use, str):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-29)    return tool_to_use
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-30)  args = task["args"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-31)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-32)    if isinstance(args, str):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-33)      resolved_args = _resolve_arg(args, observations)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-34)    elif isinstance(args, dict):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-35)      resolved_args = {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-36)        key: _resolve_arg(val, observations) for key, val in args.items()
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-37)      }
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-38)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-39)      # This will likely fail
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-40)      resolved_args = args
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-41)  except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-42)    return (
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-43)      f"ERROR(Failed to call {tool_to_use.name} with args {args}.)"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-44)      f" Args could not be resolved. Error: {repr(e)}"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-45)    )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-46)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-47)    return tool_to_use.invoke(resolved_args, config)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-48)  except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-49)    return (
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-50)      f"ERROR(Failed to call {tool_to_use.name} with args {args}."
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-51)      + f" Args resolved to {resolved_args}. Error: {repr(e)})"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-52)    )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-53)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-54)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-55)def_resolve_arg(arg: Union[str, Any], observations: Dict[int, Any]):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-56)  # $1 or ${1} -> 1
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-57)  ID_PATTERN = r"\$\{?(\d+)\}?"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-58)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-59)  defreplace_match(match):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-60)    # If the string is ${123}, match.group(0) is ${123}, and match.group(1) is 123.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-61)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-62)    # Return the match group, in this case the index, from the string. This is the index
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-63)    # number we get back.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-64)    idx = int(match.group(1))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-65)    return str(observations.get(idx, match.group(0)))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-66)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-67)  # For dependencies on other tasks
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-68)  if isinstance(arg, str):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-69)    return re.sub(ID_PATTERN, replace_match, arg)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-70)  elif isinstance(arg, list):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-71)    return [_resolve_arg(a, observations) for a in arg]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-72)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-73)    return str(arg)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-74)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-75)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-76)@as_runnable
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-77)defschedule_task(task_inputs, config):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-78)  task: Task = task_inputs["task"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-79)  observations: Dict[int, Any] = task_inputs["observations"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-80)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-81)    observation = _execute_task(task, observations, config)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-82)  except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-83)    importtraceback
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-84)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-85)    observation = traceback.format_exception() # repr(e) +
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-86)  observations[task["idx"]] = observation
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-87)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-88)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-89)defschedule_pending_task(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-90)  task: Task, observations: Dict[int, Any], retry_after: float = 0.2
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-91)):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-92)  while True:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-93)    deps = task["dependencies"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-94)    if deps and (any([dep not in observations for dep in deps])):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-95)      # Dependencies not yet satisfied
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-96)      time.sleep(retry_after)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-97)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-98)    schedule_task.invoke({"task": task, "observations": observations})
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-99)    break
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-100)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-101)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-102)@as_runnable
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-103)defschedule_tasks(scheduler_input: SchedulerInput) -> List[FunctionMessage]:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-104)"""Group the tasks into a DAG schedule."""
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-105)  # For streaming, we are making a few simplifying assumption:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-106)  # 1. The LLM does not create cyclic dependencies
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-107)  # 2. That the LLM will not generate tasks with future deps
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-108)  # If this ceases to be a good assumption, you can either
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-109)  # adjust to do a proper topological sort (not-stream)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-110)  # or use a more complicated data structure
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-111)  tasks = scheduler_input["tasks"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-112)  args_for_tasks = {}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-113)  messages = scheduler_input["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-114)  # If we are re-planning, we may have calls that depend on previous
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-115)  # plans. Start with those.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-116)  observations = _get_observations(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-117)  task_names = {}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-118)  originals = set(observations)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-119)  # ^^ We assume each task inserts a different key above to
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-120)  # avoid race conditions...
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-121)  futures = []
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-122)  retry_after = 0.25 # Retry every quarter second
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-123)  with ThreadPoolExecutor() as executor:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-124)    for task in tasks:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-125)      deps = task["dependencies"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-126)      task_names[task["idx"]] = (
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-127)        task["tool"] if isinstance(task["tool"], str) else task["tool"].name
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-128)      )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-129)      args_for_tasks[task["idx"]] = task["args"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-130)      if (
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-131)        # Depends on other tasks
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-132)        deps and (any([dep not in observations for dep in deps]))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-133)      ):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-134)        futures.append(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-135)          executor.submit(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-136)            schedule_pending_task, task, observations, retry_after
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-137)          )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-138)        )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-139)      else:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-140)        # No deps or all deps satisfied
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-141)        # can schedule now
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-142)        schedule_task.invoke(dict(task=task, observations=observations))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-143)        # futures.append(executor.submit(schedule_task.invoke, dict(task=task, observations=observations)))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-144)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-145)    # All tasks have been submitted or enqueued
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-146)    # Wait for them to complete
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-147)    wait(futures)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-148)  # Convert observations to new tool messages to add to the state
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-149)  new_observations = {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-150)    k: (task_names[k], args_for_tasks[k], observations[k])
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-151)    for k in sorted(observations.keys() - originals)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-152)  }
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-153)  tool_messages = [
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-154)    FunctionMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-155)      name=name,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-156)      content=str(obs),
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-157)      additional_kwargs={"idx": k, "args": task_args},
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-158)      tool_call_id=k,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-159)    )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-160)    for k, (name, task_args, obs) in new_observations.items()
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-161)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-17-162)  return tool_messages

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-1)importitertools
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-3)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-4)@as_runnable
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-5)defplan_and_schedule(state):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-6)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-7)  tasks = planner.stream(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-8)  # Begin executing the planner immediately
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-9)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-10)    tasks = itertools.chain([next(tasks)], tasks)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-11)  except StopIteration:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-12)    # Handle the case where tasks is empty.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-13)    tasks = iter([])
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-14)  scheduled_tasks = schedule_tasks.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-15)    {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-16)      "messages": messages,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-17)      "tasks": tasks,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-18)    }
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-19)  )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-18-20)  return {"messages": scheduled_tasks}

```


### Example Plan[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#example-plan "Permanent link")

We still haven't introduced any cycles in our computation graph, so this is all easily expressed in LCEL.

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-19-1)tool_messages = plan_and_schedule.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-19-2)  {"messages": [HumanMessage(content=example_question)]}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-19-3))["messages"]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-20-1)tool_messages

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-21-1)[FunctionMessage(content="[{'url': 'https://www.accuweather.com/en/us/san-francisco/94103/current-weather/347629', 'content': 'Get the latest weather information for San Francisco, CA, including temperature, wind, humidity, pressure, and UV index. See hourly, daily, and monthly forecasts, as ...'}]", additional_kwargs={'idx': 1, 'args': {'query': 'current temperature in San Francisco'}}, response_metadata={}, name='tavily_search_results_json', tool_call_id=1),
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-21-2) FunctionMessage(content='ValueError(\'Failed to evaluate "No specific value for \\\'x\\\' provided.". Raised error: SyntaxError(\\\'invalid syntax\\\', (\\\'<expr>\\\', 1, 4, "No specific value for \\\'x\\\' provided.", 1, 12)). Please try again with a valid numerical expression\')', additional_kwargs={'idx': 2, 'args': {'problem': 'x^3', 'context': ['$1']}}, response_metadata={}, name='math', tool_call_id=2),
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-21-3) FunctionMessage(content='join', additional_kwargs={'idx': 3, 'args': ()}, response_metadata={}, name='join', tool_call_id=3)]

```


## Joiner[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#joiner "Permanent link")

So now we have the planning and initial execution done. We need a component to process these outputs and either:

  1. Respond with the correct answer.
  2. Loop with a new plan.



The paper refers to this as the "joiner". It's another LLM call. We are using function calling to improve parsing reliability.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-1)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-2)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-3)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-4)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-5)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-6)classFinalResponse(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-7)"""The final response/answer."""
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-8)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-9)  response: str
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-10)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-11)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-12)classReplan(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-13)  feedback: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-14)    description="Analysis of the previous attempts and recommendations on what needs to be fixed."
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-15)  )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-16)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-17)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-18)classJoinOutputs(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-19)"""Decide whether to replan or whether you can return the final response."""
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-20)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-21)  thought: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-22)    description="The chain of thought reasoning for the selected action"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-23)  )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-24)  action: Union[FinalResponse, Replan]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-25)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-26)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-27)joiner_prompt = hub.pull("wfh/llm-compiler-joiner").partial(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-28)  examples=""
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-29)) # You can optionally add examples
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-30)llm = ChatOpenAI(model="gpt-4-turbo-preview")
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-31)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-32)runnable = joiner_prompt | llm.with_structured_output(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-33)  JoinOutputs, method="function_calling"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-22-34))

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html)

We will select only the most recent messages in the state, and format the output to be more useful for the planner, should the agent need to loop.

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-1)def_parse_joiner_output(decision: JoinOutputs) -> List[BaseMessage]:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-2)  response = [AIMessage(content=f"Thought: {decision.thought}")]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-3)  if isinstance(decision.action, Replan):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-4)    return {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-5)      "messages": response
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-6)      + [
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-7)        SystemMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-8)          content=f"Context from last attempt: {decision.action.feedback}"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-9)        )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-10)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-11)    }
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-12)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-13)    return {"messages": response + [AIMessage(content=decision.action.response)]}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-14)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-15)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-16)defselect_recent_messages(state) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-17)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-18)  selected = []
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-19)  for msg in messages[::-1]:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-20)    selected.append(msg)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-21)    if isinstance(msg, HumanMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-22)      break
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-23)  return {"messages": selected[::-1]}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-24)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-25)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-23-26)joiner = select_recent_messages | runnable | _parse_joiner_output

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-24-1)input_messages = [HumanMessage(content=example_question)] + tool_messages

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-25-1)joiner.invoke({"messages": input_messages})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-26-1){'messages': [AIMessage(content='Thought: Since the temperature in San Francisco was not provided, I cannot calculate its value raised to the 3rd power. The search result did not include specific temperature information, and the subsequent action to calculate the power raised the error due to lack of numerical input.', additional_kwargs={}, response_metadata={}),
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-26-2) SystemMessage(content="Context from last attempt: To answer the user's question, we need the current temperature in San Francisco. Please include a step to find the current temperature in San Francisco and then calculate its value raised to the 3rd power.", additional_kwargs={}, response_metadata={})]}

```


## Compose using LangGraph[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#compose-using-langgraph "Permanent link")

We'll define the agent as a stateful graph, with the main nodes being:

  1. Plan and execute (the DAG from the first step above)
  2. Join: determine if we should finish or replan
  3. Recontextualize: update the graph state based on the output from the joiner



```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-2)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-3)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-4)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-5)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-6)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-7)  messages: Annotated[list, add_messages]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-8)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-9)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-10)graph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-11)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-12)# 1. Define vertices
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-13)# We defined plan_and_schedule above already
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-14)# Assign each node to a state variable to update
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-15)graph_builder.add_node("plan_and_schedule", plan_and_schedule)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-16)graph_builder.add_node("join", joiner)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-17)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-18)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-19)## Define edges
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-20)graph_builder.add_edge("plan_and_schedule", "join")
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-21)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-22)### This condition determines looping logic
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-23)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-24)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-25)defshould_continue(state):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-26)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-27)  if isinstance(messages[-1], AIMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-28)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-29)  return "plan_and_schedule"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-30)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-31)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-32)graph_builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-33)  "join",
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-34)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-35)  should_continue,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-36))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-37)graph_builder.add_edge(START, "plan_and_schedule")
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-27-38)chain = graph_builder.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

### Simple question[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#simple-question "Permanent link")

Let's ask a simple question of the agent.

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-28-1)for step in chain.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-28-2)  {"messages": [HumanMessage(content="What's the GDP of New York?")]}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-28-3)):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-28-4)  print(step)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-28-5)  print("---")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-29-1){'plan_and_schedule': {'messages': [FunctionMessage(content="[{'url': 'https://www.investopedia.com/articles/investing/011516/new-yorks-economy-6-industries-driving-gdp-growth.asp', 'content': 'The manufacturing sector is a leader in railroad rolling stock, as many of the earliest railroads were financed or founded in New York; garments, as New York City is the fashion capital of the U.S.; elevator parts; glass; and many other products.\\n Educational Services\\nThough not typically thought of as a leading industry, the educational sector in New York nonetheless has a substantial impact on the state and its residents, and in attracting new talent that eventually enters the New York business scene. New York has seen a large uptick in college attendees, both young and old, over the 21st century, and an increasing number of new employees in other New York sectors were educated in the state. New York City is the leading job hub for banking, finance, and communication in the U.S. New York is also a major manufacturing center and shipping port, and it has a thriving technological sector.\\n The state of New York has the third-largest economy in the United States with a gross domestic product (GDP) of $1.7 trillion, trailing only Texas and California.'}]", additional_kwargs={'idx': 1, 'args': {'query': 'GDP of New York'}}, response_metadata={}, name='tavily_search_results_json', tool_call_id=1)]}}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-29-2)---
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-29-3){'join': {'messages': [AIMessage(content='Thought: The search result provides the specific information requested. It states that the state of New York has the third-largest economy in the United States with a GDP of $1.7 trillion.', additional_kwargs={}, response_metadata={}, id='63af07a6-f931-43e9-8fdc-4f2b8c7b7663'), AIMessage(content='The GDP of New York is $1.7 trillion.', additional_kwargs={}, response_metadata={}, id='7cfc50e6-e041-4985-a5f4-ebf2e097826e')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-29-4)---

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-30-1)# Final answer
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-30-2)print(step["join"]["messages"][-1].content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-31-1)The GDP of New York is $1.7 trillion.

```


### Multi-hop question[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#multi-hop-question "Permanent link")

This question requires that the agent perform multiple searches.

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-1)steps = chain.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-4)      HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-5)        content="What's the oldest parrot alive, and how much longer is that than the average?"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-6)      )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-7)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-8)  },
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-9)  {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-10)    "recursion_limit": 100,
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-11)  },
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-12))
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-13)for step in steps:
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-14)  print(step)
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-32-15)  print("---")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-33-1){'plan_and_schedule': {'messages': [FunctionMessage(content='[{\'url\': \'https://en.wikipedia.org/wiki/Cookie_(cockatoo)\', \'content\': \'He was one of the longest-lived birds on record[4] and was recognised by the Guinness World Records as the oldest living parrot in the world.[5]\\nThe next-oldest pink cockatoo to be found in a zoological setting was a 31-year-old female bird located at Paradise Wildlife Sanctuary, England.[3] Information published by the World Parrot Trust states longevity for Cookie\\\'s species in captivity is on average 40–60 years.[6]\\nLife[edit]\\nCookie was Brookfield Zoo\\\'s oldest resident and the last surviving member of the animal collection from the time of the zoo\\\'s opening in 1934, having arrived from Taronga Zoo of Sydney, New South Wales, Australia, in the same year and judged to be one year old at the time.[7]\\nIn the 1950s an attempt was made to introduce Cookie to a female pink cockatoo, but Cookie rejected her as "she was not nice to him".[8]\\n In 2007, Cookie was diagnosed with, and placed on medication and nutritional supplements for, osteoarthritis and osteoporosis\\xa0– medical conditions which occur commonly in aging animals and humans alike,[7] although it is believed that the latter may also have been brought on as a result of being fed a seed-only diet for the first 40 years of his life, in the years before the dietary requirements of his species were fully understood.[9]\\nCookie was "retired" from exhibition at the zoo in 2009 (following a few months of weekend-only appearances) in order to preserve his health, after it was noticed by staff that his appetite, demeanor and stress levels improved markedly when not on public display. age.[11] A memorial at the zoo was unveiled in September 2017.[12]\\nIn 2020, Cookie became the subject of a poetry collection by Barbara Gregorich entitled Cookie the Cockatoo: Everything Changes.[13]\\nSee also[edit]\\nReferences[edit]\\nExternal links[edit] He was believed to be the oldest member of his species alive in captivity, at the age of 82 in June 2015,[1]\[2] having significantly exceeded the average lifespan for his kind.[3] He was moved to a permanent residence in the keepers\\\' office of the zoo\\\'s Perching Bird House, although he made occasional appearances for special events, such as his birthday celebration, which was held each June.[3]\'}]', additional_kwargs={'idx': 1, 'args': {'query': 'oldest parrot alive'}}, response_metadata={}, name='tavily_search_results_json', tool_call_id=1), FunctionMessage(content="[{'url': 'https://www.birdzilla.com/learn/how-long-do-parrots-live/', 'content': 'In captivity, they can easily live to be ten or even 18 years of age. In general, most wild parrot species live only half the numbers of years they would live in captivity. For example, adopted African Gray Parrots might live to be 60, whereas wild birds have an average lifespan of 30 or 40 at the very most.'}]", additional_kwargs={'idx': 2, 'args': {'query': 'average lifespan of a parrot'}}, response_metadata={}, name='tavily_search_results_json', tool_call_id=2), FunctionMessage(content='join', additional_kwargs={'idx': 3, 'args': ()}, response_metadata={}, name='join', tool_call_id=3)]}}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-33-2)---
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-33-3){'join': {'messages': [AIMessage(content="Thought: The information from Wikipedia about Cookie, the cockatoo, indicates that he was recognized as the oldest living parrot, reaching the age of 82. This significantly exceeds the average lifespan for his species, which is noted to be 40-60 years in captivity. The information from Birdzilla provides a more general perspective on parrot lifespans, indicating that, in captivity, parrots can easily live to be ten or even 18 years of age, with some species like the African Gray Parrot potentially living up to 60 years. However, it does not provide a specific average lifespan for all parrot species, making it challenging to provide a precise comparison for Cookie's age beyond his species' average lifespan.", additional_kwargs={}, response_metadata={}, id='f00a464e-c273-42b9-8d1b-edd27bde8687'), AIMessage(content="Cookie the cockatoo was recognized as the oldest living parrot, reaching the age of 82, which is significantly beyond the average lifespan for his species, noted to be between 40-60 years in captivity. While general information for parrots suggests varying lifespans with some capable of living up to 60 years in captivity, Cookie's age far exceeded these averages, highlighting his exceptional longevity.", additional_kwargs={}, response_metadata={}, id='dc62a826-5528-446e-8797-6854abdeb94c')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-33-4)---

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-34-1)# Final answer
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-34-2)print(step["join"]["messages"][-1].content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-35-1)Cookie the cockatoo was recognized as the oldest living parrot, reaching the age of 82, which is significantly beyond the average lifespan for his species, noted to be between 40-60 years in captivity. While general information for parrots suggests varying lifespans with some capable of living up to 60 years in captivity, Cookie's age far exceeded these averages, highlighting his exceptional longevity.

```


### Multi-step math[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#multi-step-math "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-1)for step in chain.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-4)      HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-5)        content="What's ((3*(4+5)/0.5)+3245) + 8? What's 32/4.23? What's the sum of those two values?"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-6)      )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-7)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-8)  }
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-9)):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-36-10)  print(step)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-37-1){'plan_and_schedule': {'messages': [FunctionMessage(content='3307.0', additional_kwargs={'idx': 1, 'args': {'problem': '((3*(4+5)/0.5)+3245) + 8'}}, response_metadata={}, name='math', tool_call_id=1), FunctionMessage(content='7.565011820330969', additional_kwargs={'idx': 2, 'args': {'problem': '32/4.23'}}, response_metadata={}, name='math', tool_call_id=2), FunctionMessage(content='join', additional_kwargs={'idx': 3, 'args': ()}, response_metadata={}, name='join', tool_call_id=3)]}}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-37-2){'join': {'messages': [AIMessage(content="Thought: The calculations for both the expressions provided by the user have been successfully completed, with the results being 3307.0 for the first expression and 7.565011820330969 for the second. Therefore, we have all the necessary information to answer the user's question.", additional_kwargs={}, response_metadata={}, id='2dd394b3-468a-4abc-b7d2-02f7b803a8b6'), AIMessage(content='The result of the first calculation ((3*(4+5)/0.5)+3245) + 8 is 3307.0, and the result of the second calculation (32/4.23) is approximately 7.57. The sum of those two values is 3307.0 + 7.57 = approximately 3314.57.', additional_kwargs={}, response_metadata={}, id='83eb8e01-7a0a-4f79-8475-fad5bc83e645')]}}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-38-1)# Final answer
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-38-2)print(step["join"]["messages"][-1].content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-39-1)The result of the first calculation ((3*(4+5)/0.5)+3245) + 8 is 3307.0, and the result of the second calculation (32/4.23) is approximately 7.57. The sum of those two values is 3307.0 + 7.57 = approximately 3314.57.

```


### Complex Replanning Example[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#complex-replanning-example "Permanent link")

This question is likely to prompt the Replan functionality, but it may need to be run multiple times to see this in action.

```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-1)for step in chain.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-4)      HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-5)        content="Find the current temperature in Tokyo, then, respond with a flashcard summarizing this information"
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-6)      )
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-7)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-8)  }
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-9)):
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-40-10)  print(step)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-41-1){'plan_and_schedule': {'messages': [FunctionMessage(content="[{'url': 'https://www.timeanddate.com/weather/japan/tokyo/ext', 'content': 'Tokyo 14 Day Extended Forecast. Weather Today Weather Hourly 14 Day Forecast Yesterday/Past Weather Climate (Averages) Currently: 84 °F. Partly sunny. (Weather station: Tokyo, Japan). See more current weather.'}]", additional_kwargs={'idx': 1, 'args': {'query': 'current temperature in Tokyo'}}, response_metadata={}, name='tavily_search_results_json', tool_call_id=1), FunctionMessage(content='join', additional_kwargs={'idx': 2, 'args': ()}, response_metadata={}, name='join', tool_call_id=2)]}}
[](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__codelineno-41-2){'join': {'messages': [AIMessage(content='Thought: The extracted information provides the current temperature in Tokyo, which is 84 °F and describes the weather as partly sunny. This information is sufficient to create a flashcard summary for the user.', additional_kwargs={}, response_metadata={}, id='e9a1af40-ca06-4eb8-b4bb-24429cf8c689'), AIMessage(content='**Flashcard: Current Temperature in Tokyo**\n\n- **Temperature:** 84 °F\n- **Weather Conditions:** Partly sunny\n\n*Note: This information is based on the latest available data and may change.*', additional_kwargs={}, response_metadata={}, id='92bb42bc-e9b9-4b98-8936-8f74ff111504')]}}

```


## Conclusion[¶](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#conclusion "Permanent link")

Congrats on building your first LLMCompiler agent! I'll leave you with some known limitations to the implementation above:

  1. The planner output parsing format is fragile if your function requires more than 1 or 2 arguments. We could make it more robust by using streaming tool calling.
  2. Variable substitution is fragile in the example above. It could be made more robust by using a fine-tuned model and a more robust syntax (using e.g., Lark or a tool calling schema)
  3. The state can grow quite long if you require multiple re-planning runs. To handle, you could add a message compressor once you go above a certain token limit.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Reasoning without Observation  ](https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/) [ Next  Reflection  ](https://langchain-ai.github.io/langgraph/tutorials/reflection/reflection/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
