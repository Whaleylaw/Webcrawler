---
url: https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#complex-data-extraction-with-function-calling)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Complex data extraction with function calling 

[ ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/?q= "Share")

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
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)
        * Experimental  Experimental 
          * [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)
          * [ Web Research (STORM)  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/)
          * [ TNT-LLM: Text Mining at Scale  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/)
          * [ Web Voyager  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/)
          * [ Competitive Programming  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/)
          * Complex data extraction with function calling  [ Complex data extraction with function calling  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#setup)
            * [ Regular Extraction with Retries  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#regular-extraction-with-retries)
              * [ Define the Validator + Retry Graph  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#define-the-validator-retry-graph)
              * [ Try it out  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#try-it-out)
                * [ Nested Examples  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#nested-examples)
            * [ JSONPatch  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#jsonpatch)
              * [ And it works!  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#and-it-works)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#setup)
  * [ Regular Extraction with Retries  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#regular-extraction-with-retries)
    * [ Define the Validator + Retry Graph  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#define-the-validator-retry-graph)
    * [ Try it out  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#try-it-out)
      * [ Nested Examples  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#nested-examples)
  * [ JSONPatch  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#jsonpatch)
    * [ And it works!  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#and-it-works)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/extraction/retries.ipynb "Edit this page")

# Complex data extraction with function calling[¶](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#complex-data-extraction-with-function-calling "Permanent link")

Function calling is a core primitive for integrating LLMs within your software stack. We use it throughout the LangGraph docs, since developing with function calling (aka tool usage) tends to be much more stress-free than the traditional way of writing custom string parsers.

However, even GPT-4, Opus, and other powerful models still struggle with complex functions, especially if your schema involves any nesting or if you have more advanced data validation rules.

There are three basic ways to increase reliability: better prompting, constrained decoding, and **validation with re-prompting**.

We will cover two approaches to the last technique here, since it is generally applicable across any LLM that supports tool calling.

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-0-2)%pip install -U langchain-anthropic langgraph

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Regular Extraction with Retries[¶](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#regular-extraction-with-retries "Permanent link")

Both examples here invoke a simple looping graph that takes following approach: 1. Prompt the LLM to respond. 2. If it responds with tool calls, validate those. 3. If the calls are correct, return. Otherwise, format the validation error as a new [ToolMessage](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.tool.ToolMessage.html#langchain_core.messages.tool.ToolMessage) and prompt the LLM to fix the errors. Taking us back to step (1).

The techniques differ only on step (3). In this first step, we will prompt the original LLM to regenerate the function calls to fix the validation errors. In the next section, we will instead prompt the LLM to generate a **patch** to fix the errors, meaning it doesn't have to re-generate data that is valid.

### Define the Validator + Retry Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#define-the-validator-retry-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-1)importoperator
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-2)importuuid
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-3)fromtypingimport (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-4)  Annotated,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-5)  Any,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-6)  Callable,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-7)  Dict,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-8)  List,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-9)  Literal,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-10)  Optional,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-11)  Sequence,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-12)  Type,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-13)  Union,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-14))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-16)fromlangchain_core.language_modelsimport BaseChatModel
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-17)fromlangchain_core.messagesimport (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-18)  AIMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-19)  AnyMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-20)  BaseMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-21)  HumanMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-22)  ToolCall,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-23))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-24)fromlangchain_core.prompt_valuesimport PromptValue
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-25)fromlangchain_core.runnablesimport (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-26)  Runnable,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-27)  RunnableLambda,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-28))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-29)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-30)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-31)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-32)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-33)fromlanggraph.prebuiltimport ValidationNode
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-35)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-36)def_default_aggregator(messages: Sequence[AnyMessage]) -> AIMessage:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-37)  for m in messages[::-1]:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-38)    if m.type == "ai":
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-39)      return m
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-40)  raise ValueError("No AI message found in the sequence.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-41)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-42)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-43)classRetryStrategy(TypedDict, total=False):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-44)"""The retry strategy for a tool call."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-45)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-46)  max_attempts: int
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-47)"""The maximum number of attempts to make."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-48)  fallback: Optional[
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-49)    Union[
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-50)      Runnable[Sequence[AnyMessage], AIMessage],
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-51)      Runnable[Sequence[AnyMessage], BaseMessage],
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-52)      Callable[[Sequence[AnyMessage]], AIMessage],
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-53)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-54)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-55)"""The function to use once validation fails."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-56)  aggregate_messages: Optional[Callable[[Sequence[AnyMessage]], AIMessage]]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-57)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-58)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-59)def_bind_validator_with_retries(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-60)  llm: Union[
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-61)    Runnable[Sequence[AnyMessage], AIMessage],
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-62)    Runnable[Sequence[BaseMessage], BaseMessage],
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-63)  ],
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-64)  *,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-65)  validator: ValidationNode,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-66)  retry_strategy: RetryStrategy,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-67)  tool_choice: Optional[str] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-68)) -> Runnable[Union[List[AnyMessage], PromptValue], AIMessage]:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-69)"""Binds a tool validators + retry logic to create a runnable validation graph.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-70)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-71)  LLMs that support tool calling can generate structured JSON. However, they may not always
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-72)  perfectly follow your requested schema, especially if the schema is nested or has complex
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-73)  validation rules. This method allows you to bind a validation function to the LLM's output,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-74)  so that any time the LLM generates a message, the validation function is run on it. If
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-75)  the validation fails, the method will retry the LLM with a fallback strategy, the simplest
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-76)  being just to add a message to the output with the validation errors and a request to fix them.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-77)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-78)  The resulting runnable expects a list of messages as input and returns a single AI message.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-79)  By default, the LLM can optionally NOT invoke tools, making this easier to incorporate into
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-80)  your existing chat bot. You can specify a tool_choice to force the validator to be run on
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-81)  the outputs.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-82)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-83)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-84)    llm (Runnable): The llm that will generate the initial messages (and optionally fallba)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-85)    validator (ValidationNode): The validation logic.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-86)    retry_strategy (RetryStrategy): The retry strategy to use.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-87)      Possible keys:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-88)      - max_attempts: The maximum number of attempts to make.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-89)      - fallback: The LLM or function to use in case of validation failure.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-90)      - aggregate_messages: A function to aggregate the messages over multiple turns.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-91)        Defaults to fetching the last AI message.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-92)    tool_choice: If provided, always run the validator on the tool output.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-93)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-94)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-95)    Runnable: A runnable that can be invoked with a list of messages and returns a single AI message.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-96)  """
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-97)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-98)  defadd_or_overwrite_messages(left: list, right: Union[list, dict]) -> list:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-99)"""Append messages. If the update is a 'finalized' output, replace the whole list."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-100)    if isinstance(right, dict) and "finalize" in right:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-101)      finalized = right["finalize"]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-102)      if not isinstance(finalized, list):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-103)        finalized = [finalized]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-104)      for m in finalized:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-105)        if m.id is None:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-106)          m.id = str(uuid.uuid4())
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-107)      return finalized
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-108)    res = add_messages(left, right)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-109)    if not isinstance(res, list):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-110)      return [res]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-111)    return res
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-112)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-113)  classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-114)    messages: Annotated[list, add_or_overwrite_messages]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-115)    attempt_number: Annotated[int, operator.add]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-116)    initial_num_messages: int
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-117)    input_format: Literal["list", "dict"]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-118)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-119)  builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-120)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-121)  defdedict(x: State) -> list:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-122)"""Get the messages from the state."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-123)    return x["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-124)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-125)  model = dedict | llm | (lambda msg: {"messages": [msg], "attempt_number": 1})
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-126)  fbrunnable = retry_strategy.get("fallback")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-127)  if fbrunnable is None:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-128)    fb_runnable = llm
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-129)  elif isinstance(fbrunnable, Runnable):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-130)    fb_runnable = fbrunnable # type: ignore
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-131)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-132)    fb_runnable = RunnableLambda(fbrunnable)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-133)  fallback = (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-134)    dedict | fb_runnable | (lambda msg: {"messages": [msg], "attempt_number": 1})
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-135)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-136)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-137)  defcount_messages(state: State) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-138)    return {"initial_num_messages": len(state.get("messages", []))}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-139)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-140)  builder.add_node("count_messages", count_messages)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-141)  builder.add_node("llm", model)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-142)  builder.add_node("fallback", fallback)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-143)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-144)  # To support patch-based retries, we need to be able to
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-145)  # aggregate the messages over multiple turns.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-146)  # The next sequence selects only the relevant messages
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-147)  # and then applies the validator
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-148)  select_messages = retry_strategy.get("aggregate_messages") or _default_aggregator
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-149)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-150)  defselect_generated_messages(state: State) -> list:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-151)"""Select only the messages generated within this loop."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-152)    selected = state["messages"][state["initial_num_messages"] :]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-153)    return [select_messages(selected)]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-154)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-155)  defendict_validator_output(x: Sequence[AnyMessage]) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-156)    if tool_choice and not x:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-157)      return {
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-158)        "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-159)          HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-160)            content=f"ValidationError: please respond with a valid tool call [tool_choice={tool_choice}].",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-161)            additional_kwargs={"is_error": True},
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-162)          )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-163)        ]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-164)      }
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-165)    return {"messages": x}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-166)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-167)  validator_runnable = select_generated_messages | validator | endict_validator_output
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-168)  builder.add_node("validator", validator_runnable)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-169)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-170)  classFinalizer:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-171)"""Pick the final message to return from the retry loop."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-172)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-173)    def__init__(self, aggregator: Optional[Callable[[list], AIMessage]] = None):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-174)      self._aggregator = aggregator or _default_aggregator
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-175)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-176)    def__call__(self, state: State) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-177)"""Return just the AI message."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-178)      initial_num_messages = state["initial_num_messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-179)      generated_messages = state["messages"][initial_num_messages:]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-180)      return {
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-181)        "messages": {
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-182)          "finalize": self._aggregator(generated_messages),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-183)        }
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-184)      }
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-185)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-186)  # We only want to emit the final message
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-187)  builder.add_node("finalizer", Finalizer(retry_strategy.get("aggregate_messages")))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-188)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-189)  # Define the connectivity
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-190)  builder.add_edge(START, "count_messages")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-191)  builder.add_edge("count_messages", "llm")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-192)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-193)  defroute_validator(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-194)    if state["messages"][-1].tool_calls or tool_choice is not None:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-195)      return "validator"
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-196)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-197)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-198)  builder.add_conditional_edges("llm", route_validator, ["validator", END])
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-199)  builder.add_edge("fallback", "validator")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-200)  max_attempts = retry_strategy.get("max_attempts", 3)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-201)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-202)  defroute_validation(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-203)    if state["attempt_number"] > max_attempts:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-204)      raise ValueError(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-205)        f"Could not extract a valid value in {max_attempts} attempts."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-206)      )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-207)    for m in state["messages"][::-1]:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-208)      if m.type == "ai":
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-209)        break
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-210)      if m.additional_kwargs.get("is_error"):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-211)        return "fallback"
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-212)    return "finalizer"
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-213)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-214)  builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-215)    "validator", route_validation, ["finalizer", "fallback"]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-216)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-217)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-218)  builder.add_edge("finalizer", END)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-219)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-220)  # These functions let the step be used in a MessageGraph
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-221)  # or a StateGraph with 'messages' as the key.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-222)  defencode(x: Union[Sequence[AnyMessage], PromptValue]) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-223)"""Ensure the input is the correct format."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-224)    if isinstance(x, PromptValue):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-225)      return {"messages": x.to_messages(), "input_format": "list"}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-226)    if isinstance(x, list):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-227)      return {"messages": x, "input_format": "list"}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-228)    raise ValueError(f"Unexpected input type: {type(x)}")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-229)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-230)  defdecode(x: State) -> AIMessage:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-231)"""Ensure the output is in the expected format."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-232)    return x["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-233)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-234)  return (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-235)    encode | builder.compile().with_config(run_name="ValidationGraph") | decode
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-236)  ).with_config(run_name="ValidateWithRetries")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-237)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-238)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-239)defbind_validator_with_retries(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-240)  llm: BaseChatModel,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-241)  *,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-242)  tools: list,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-243)  tool_choice: Optional[str] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-244)  max_attempts: int = 3,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-245)) -> Runnable[Union[List[AnyMessage], PromptValue], AIMessage]:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-246)"""Binds validators + retry logic ensure validity of generated tool calls.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-247)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-248)  LLMs that support tool calling are good at generating structured JSON. However, they may
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-249)  not always perfectly follow your requested schema, especially if the schema is nested or
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-250)  has complex validation rules. This method allows you to bind a validation function to
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-251)  the LLM's output, so that any time the LLM generates a message, the validation function
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-252)  is run on it. If the validation fails, the method will retry the LLM with a fallback
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-253)  strategy, the simples being just to add a message to the output with the validation
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-254)  errors and a request to fix them.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-255)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-256)  The resulting runnable expects a list of messages as input and returns a single AI message.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-257)  By default, the LLM can optionally NOT invoke tools, making this easier to incorporate into
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-258)  your existing chat bot. You can specify a tool_choice to force the validator to be run on
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-259)  the outputs.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-260)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-261)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-262)    llm (Runnable): The llm that will generate the initial messages (and optionally fallba)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-263)    validator (ValidationNode): The validation logic.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-264)    retry_strategy (RetryStrategy): The retry strategy to use.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-265)      Possible keys:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-266)      - max_attempts: The maximum number of attempts to make.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-267)      - fallback: The LLM or function to use in case of validation failure.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-268)      - aggregate_messages: A function to aggregate the messages over multiple turns.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-269)        Defaults to fetching the last AI message.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-270)    tool_choice: If provided, always run the validator on the tool output.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-271)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-272)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-273)    Runnable: A runnable that can be invoked with a list of messages and returns a single AI message.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-274)  """
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-275)  bound_llm = llm.bind_tools(tools, tool_choice=tool_choice)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-276)  retry_strategy = RetryStrategy(max_attempts=max_attempts)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-277)  validator = ValidationNode(tools)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-278)  return _bind_validator_with_retries(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-279)    bound_llm,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-280)    validator=validator,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-281)    tool_choice=tool_choice,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-282)    retry_strategy=retry_strategy,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-2-283)  ).with_config(metadata={"retry_strategy": "default"})

```


API Reference: [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html) | [PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

### Try it out[¶](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#try-it-out "Permanent link")

Now we'll ask our model to call a function. We'll add a validator to illustrate how the LLM is able to use the validation error to fix its results.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-1)frompydanticimport BaseModel, Field, field_validator
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-4)classRespond(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-5)"""Use to generate the response. Always use when responding to the user"""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-7)  reason: str = Field(description="Step-by-step justification for the answer.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-8)  answer: str
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-10)  @field_validator("answer")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-11)  defreason_contains_apology(cls, answer: str):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-12)    if "llama" not in answer.lower():
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-13)      raise ValueError(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-14)        "You MUST start with a gimicky, rhyming advertisement for using a Llama V3 (an LLM) in your **answer** field."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-15)        " Must be an instant hit. Must be weaved into the answer."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-16)      )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-3-19)tools = [Respond]

```


Create the LLM.

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-1)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-2)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-4)# Or you can use ChatGroq, ChatOpenAI, ChatGoogleGemini, ChatCohere, etc.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-5)# See https://python.langchain.com/docs/integrations/chat/ for more info on tool calling
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-6)llm = ChatAnthropic(model="claude-3-haiku-20240307")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-7)bound_llm = bind_validator_with_retries(llm, tools=tools)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-8)prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-9)  [
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-10)    ("system", "Respond directly by calling the Respond function."),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-11)    ("placeholder", "{messages}"),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-12)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-13))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-4-15)chain = prompt | bound_llm

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-5-1)results = chain.invoke({"messages": [("user", "Does P = NP?")]})
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-5-2)results.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-3)[{'text': 'Okay, let me try this again with a fun rhyming advertisement:', 'type': 'text'}, {'id': 'toolu_01ACZEPYEyqmpf3kA4VERXFY', 'input': {'answer': "With a Llama V3, the answer you'll see,\nWhether P equals NP is a mystery!\nThe class P and NP, a puzzle so grand,\nSolved or unsolved, the future's at hand.\nThe question remains, unanswered for now,\nBut with a Llama V3, we'll find out how!", 'reason': 'The question of whether P = NP is one of the most famous unsolved problems in computer science and mathematics. P and NP are complexity classes that describe how quickly problems can be solved by computers.\n\nThe P class contains problems that can be solved in polynomial time, meaning the time to solve the problem scales polynomially with the size of the input. The NP class contains problems where the solution can be verified in polynomial time, but there may not be a polynomial time algorithm to find the solution. \n\nWhether P = NP is an open question - it is not known if every problem in NP can also be solved in polynomial time. If P = NP, it would mean that all problems with quickly verifiable solutions could also be quickly solved, which would have major implications for computing and cryptography. However, most experts believe that P ≠ NP, meaning some problems in NP are harder than P-class problems and cannot be solved efficiently. This is considered one of the hardest unsolved problems in mathematics.'}, 'name': 'Respond', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-4)Tool Calls:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-5) Respond (toolu_01ACZEPYEyqmpf3kA4VERXFY)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-6) Call ID: toolu_01ACZEPYEyqmpf3kA4VERXFY
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-7) Args:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-8)  answer: With a Llama V3, the answer you'll see,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-9)Whether P equals NP is a mystery!
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-10)The class P and NP, a puzzle so grand,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-11)Solved or unsolved, the future's at hand.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-12)The question remains, unanswered for now,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-13)But with a Llama V3, we'll find out how!
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-14)  reason: The question of whether P = NP is one of the most famous unsolved problems in computer science and mathematics. P and NP are complexity classes that describe how quickly problems can be solved by computers.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-15)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-16)The P class contains problems that can be solved in polynomial time, meaning the time to solve the problem scales polynomially with the size of the input. The NP class contains problems where the solution can be verified in polynomial time, but there may not be a polynomial time algorithm to find the solution. 
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-17)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-6-18)Whether P = NP is an open question - it is not known if every problem in NP can also be solved in polynomial time. If P = NP, it would mean that all problems with quickly verifiable solutions could also be quickly solved, which would have major implications for computing and cryptography. However, most experts believe that P ≠ NP, meaning some problems in NP are harder than P-class problems and cannot be solved efficiently. This is considered one of the hardest unsolved problems in mathematics.

```


#### Nested Examples[¶](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#nested-examples "Permanent link")

So you can see that it's able to recover when its first generation is incorrect, great! But is it bulletproof?

Not so much. Let's try it out on a complex nested schema.

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-1)fromtypingimport List, Optional
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-4)classOutputFormat(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-5)  sources: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-6)    ...,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-7)    description="The raw transcript / span you could cite to justify the choice.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-8)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-9)  content: str = Field(..., description="The chosen value.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-12)classMoment(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-13)  quote: str = Field(..., description="The relevant quote from the transcript.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-14)  description: str = Field(..., description="A description of the moment.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-15)  expressed_preference: OutputFormat = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-16)    ..., description="The preference expressed in the moment."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-17)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-18)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-19)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-20)classBackgroundInfo(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-21)  factoid: OutputFormat = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-22)    ..., description="Important factoid about the member."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-23)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-24)  professions: list
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-25)  why: str = Field(..., description="Why this is important.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-27)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-28)classKeyMoments(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-29)  topic: str = Field(..., description="The topic of the key moments.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-30)  happy_moments: List[Moment] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-31)    ..., description="A list of key moments related to the topic."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-32)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-33)  tense_moments: List[Moment] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-34)    ..., description="Moments where things were a bit tense."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-35)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-36)  sad_moments: List[Moment] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-37)    ..., description="Moments where things where everyone was downtrodden."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-38)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-39)  background_info: list[BackgroundInfo]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-40)  moments_summary: str = Field(..., description="A summary of the key moments.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-41)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-42)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-43)classMember(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-44)  name: OutputFormat = Field(..., description="The name of the member.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-45)  role: Optional[str] = Field(None, description="The role of the member.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-46)  age: Optional[int] = Field(None, description="The age of the member.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-47)  background_details: List[BackgroundInfo] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-48)    ..., description="A list of background details about the member."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-49)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-50)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-51)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-52)classInsightfulQuote(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-53)  quote: OutputFormat = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-54)    ..., description="An insightful quote from the transcript."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-55)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-56)  speaker: str = Field(..., description="The name of the speaker who said the quote.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-57)  analysis: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-58)    ..., description="An analysis of the quote and its significance."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-59)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-60)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-61)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-62)classTranscriptMetadata(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-63)  title: str = Field(..., description="The title of the transcript.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-64)  location: OutputFormat = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-65)    ..., description="The location where the interview took place."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-66)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-67)  duration: str = Field(..., description="The duration of the interview.")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-68)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-69)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-70)classTranscriptSummary(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-71)  metadata: TranscriptMetadata = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-72)    ..., description="Metadata about the transcript."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-73)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-74)  participants: List[Member] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-75)    ..., description="A list of participants in the interview."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-76)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-77)  key_moments: List[KeyMoments] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-78)    ..., description="A list of key moments from the interview."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-79)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-80)  insightful_quotes: List[InsightfulQuote] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-81)    ..., description="A list of insightful quotes from the interview."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-82)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-83)  overall_summary: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-84)    ..., description="An overall summary of the interview."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-85)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-86)  next_steps: List[str] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-87)    ..., description="A list of next steps or action items based on the interview."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-88)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-7-89)  other_stuff: List[OutputFormat]

```


Let's see how it does on this made up transcript.

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-1)transcript = [
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-2)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-3)    "Pete",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-4)    "Hey Xu, Laura, thanks for hopping on this call. I've been itching to talk about this Drake and Kendrick situation.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-5)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-6)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-7)    "Xu",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-8)    "No problem. As its my job, I've got some thoughts on this beef.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-9)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-10)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-11)    "Laura",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-12)    "Yeah, I've got some insider info so this should be interesting.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-13)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-14)  ("Pete", "Dope. So, when do you think this whole thing started?"),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-15)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-16)    "Pete",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-17)    "Definitely was Kendrick's 'Control' verse that kicked it off.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-18)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-19)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-20)    "Laura",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-21)    "Truth, but Drake never went after him directly. Just some subtle jabs here and there.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-22)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-23)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-24)    "Xu",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-25)    "That's the thing with beefs like this, though. They've always been a a thing, pushing artists to step up their game.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-26)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-27)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-28)    "Pete",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-29)    "For sure, and this beef has got the fans taking sides. Some are all about Drake's mainstream appeal, while others are digging Kendrick's lyrical skills.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-30)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-31)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-32)    "Laura",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-33)    "I mean, Drake knows how to make a hit that gets everyone hyped. That's his thing.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-34)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-35)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-36)    "Pete",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-37)    "I hear you, Laura, but I gotta give it to Kendrick when it comes to straight-up bars. The man's a beast on the mic.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-38)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-39)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-40)    "Xu",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-41)    "It's wild how this beef is shaping fans.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-42)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-43)  ("Pete", "do you think these beefs can actually be good for hip-hop?"),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-44)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-45)    "Xu",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-46)    "Hell yeah, Pete. When it's done right, a beef can push the genre forward and make artists level up.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-47)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-48)  ("Laura", "eh"),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-49)  ("Pete", "So, where do you see this beef going?"),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-50)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-51)    "Laura",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-52)    "Honestly, I think it'll stay a hot topic for the fans, but unless someone drops a straight-up diss track, it's not gonna escalate.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-53)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-54)  ("Laura", "ehhhhhh not sure"),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-55)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-56)    "Pete",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-57)    "I feel that. I just want both of them to keep dropping heat, beef or no beef.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-58)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-59)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-60)    "Xu",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-61)    "I'm curious. May influence a lot of people. Make things more competitive. Bring on a whole new wave of lyricism.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-62)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-63)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-64)    "Pete",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-65)    "Word. Hey, thanks for chopping it up with me, Xu and Laura. This was dope.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-66)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-67)  ("Xu", "Where are you going so fast?"),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-68)  (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-69)    "Laura",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-70)    "For real, I had a good time. Nice to get different perspectives on the situation.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-71)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-72)]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-73)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-8-74)formatted = "\n".join(f"{x[0]}: {x[1]}" for x in transcript)

```


Now, run our model. We **expect** GPT turbo to still fail on this challenging template.

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-1)tools = [TranscriptSummary]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-2)bound_llm = bind_validator_with_retries(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-3)  llm,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-4)  tools=tools,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-5))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-6)prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-7)  [
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-8)    ("system", "Respond directly using the TranscriptSummary function."),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-9)    ("placeholder", "{messages}"),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-10)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-11))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-12)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-13)chain = prompt | bound_llm
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-15)try:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-16)  results = chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-17)    {
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-18)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-19)        (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-20)          "user",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-21)          f"Extract the summary from the following conversation:\n\n<convo>\n{formatted}\n</convo>"
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-22)          "\n\nRemember to respond using the TranscriptSummary function.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-23)        )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-24)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-25)    },
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-26)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-27)  results.pretty_print()
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-28)except ValueError as e:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-9-29)  print(repr(e))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-10-1)ValueError('Could not extract a valid value in 3 attempts.')

```


## JSONPatch[¶](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#jsonpatch "Permanent link")

The regular retry method worked well for our simple case, but it still was unable to self-correct when populating a complex schema.

LLMs work best on narrow tasks. A tried-and-true principle of LLM interface design is to simplify the task for each LLM run.

One way to do this is to **patch** the state instead of completely regenerating the state. One way to do this is with `JSONPatch` operations. Let's try it out!

Below, create a JSONPatch retry graph. This works as follows: 1. First pass: try to generate the full output. 2. Retries: prompt the LLM to generate **JSON patches** on top of the first output to heal the erroneous generation.

The fallback LLM just has to generate a list of paths, ops (add, remove, replace), and optional values. Since the pydantic validation errors include the path in their errors, the LLM should be more reliable.

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-11-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-11-2)%pip install -U jsonpatch

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-1)importlogging
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-3)logger = logging.getLogger("extraction")
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-6)defbind_validator_with_jsonpatch_retries(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-7)  llm: BaseChatModel,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-8)  *,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-9)  tools: list,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-10)  tool_choice: Optional[str] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-11)  max_attempts: int = 3,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-12)) -> Runnable[Union[List[AnyMessage], PromptValue], AIMessage]:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-13)"""Binds validators + retry logic ensure validity of generated tool calls.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-14)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-15)  This method is similar to `bind_validator_with_retries`, but uses JSONPatch to correct
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-16)  validation errors caused by passing in incorrect or incomplete parameters in a previous
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-17)  tool call. This method requires the 'jsonpatch' library to be installed.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-18)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-19)  Using patch-based function healing can be more efficient than repopulating the entire
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-20)  tool call from scratch, and it can be an easier task for the LLM to perform, since it typically
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-21)  only requires a few small changes to the existing tool call.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-22)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-23)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-24)    llm (Runnable): The llm that will generate the initial messages (and optionally fallba)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-25)    tools (list): The tools to bind to the LLM.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-26)    tool_choice (Optional[str]): The tool choice to use.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-27)    max_attempts (int): The number of attempts to make.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-28)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-29)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-30)    Runnable: A runnable that can be invoked with a list of messages and returns a single AI message.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-31)  """
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-32)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-33)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-34)    importjsonpatch # type: ignore[import-untyped]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-35)  except ImportError:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-36)    raise ImportError(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-37)      "The 'jsonpatch' library is required for JSONPatch-based retries."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-38)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-39)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-40)  classJsonPatch(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-41)"""A JSON Patch document represents an operation to be performed on a JSON document.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-42)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-43)    Note that the op and path are ALWAYS required. Value is required for ALL operations except 'remove'.
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-44)    Examples:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-45)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-46)    \`\`\`json
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-47)    {"op": "add", "path": "/a/b/c", "patch_value": 1}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-48)    {"op": "replace", "path": "/a/b/c", "patch_value": 2}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-49)    {"op": "remove", "path": "/a/b/c"}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-50)    \`\`\`
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-51)    """
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-52)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-53)    op: Literal["add", "remove", "replace"] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-54)      ...,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-55)      description="The operation to be performed. Must be one of 'add', 'remove', 'replace'.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-56)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-57)    path: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-58)      ...,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-59)      description="A JSON Pointer path that references a location within the target document where the operation is performed.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-60)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-61)    value: Any = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-62)      ...,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-63)      description="The value to be used within the operation. REQUIRED for 'add', 'replace', and 'test' operations.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-64)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-65)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-66)  classPatchFunctionParameters(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-67)"""Respond with all JSONPatch operation to correct validation errors caused by passing in incorrect or incomplete parameters in a previous tool call."""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-68)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-69)    tool_call_id: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-70)      ...,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-71)      description="The ID of the original tool call that generated the error. Must NOT be an ID of a PatchFunctionParameters tool call.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-72)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-73)    reasoning: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-74)      ...,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-75)      description="Think step-by-step, listing each validation error and the"
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-76)      " JSONPatch operation needed to correct it. "
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-77)      "Cite the fields in the JSONSchema you referenced in developing this plan.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-78)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-79)    patches: list[JsonPatch] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-80)      ...,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-81)      description="A list of JSONPatch operations to be applied to the previous tool call's response.",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-82)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-83)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-84)  bound_llm = llm.bind_tools(tools, tool_choice=tool_choice)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-85)  fallback_llm = llm.bind_tools([PatchFunctionParameters])
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-86)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-87)  defaggregate_messages(messages: Sequence[AnyMessage]) -> AIMessage:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-88)    # Get all the AI messages and apply json patches
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-89)    resolved_tool_calls: Dict[Union[str, None], ToolCall] = {}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-90)    content: Union[str, List[Union[str, dict]]] = ""
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-91)    for m in messages:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-92)      if m.type != "ai":
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-93)        continue
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-94)      if not content:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-95)        content = m.content
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-96)      for tc in m.tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-97)        if tc["name"] == PatchFunctionParameters.__name__:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-98)          tcid = tc["args"]["tool_call_id"]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-99)          if tcid not in resolved_tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-100)            logger.debug(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-101)              f"JsonPatch tool call ID {tc['args']['tool_call_id']} not found."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-102)              f"Valid tool call IDs: {list(resolved_tool_calls.keys())}"
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-103)            )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-104)            tcid = next(iter(resolved_tool_calls.keys()), None)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-105)          orig_tool_call = resolved_tool_calls[tcid]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-106)          current_args = orig_tool_call["args"]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-107)          patches = tc["args"].get("patches") or []
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-108)          orig_tool_call["args"] = jsonpatch.apply_patch(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-109)            current_args,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-110)            patches,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-111)          )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-112)          orig_tool_call["id"] = tc["id"]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-113)        else:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-114)          resolved_tool_calls[tc["id"]] = tc.copy()
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-115)    return AIMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-116)      content=content,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-117)      tool_calls=list(resolved_tool_calls.values()),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-118)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-119)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-120)  defformat_exception(error: BaseException, call: ToolCall, schema: Type[BaseModel]):
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-121)    return (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-122)      f"Error:\n\n\`\`\`\n{repr(error)}\n\`\`\`\n"
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-123)      "Expected Parameter Schema:\n\n" + f"\`\`\`json\n{schema.schema_json()}\n\`\`\`\n"
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-124)      f"Please respond with a JSONPatch to correct the error for tool_call_id=[{call['id']}]."
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-125)    )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-126)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-127)  validator = ValidationNode(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-128)    tools + [PatchFunctionParameters],
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-129)    format_error=format_exception,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-130)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-131)  retry_strategy = RetryStrategy(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-132)    max_attempts=max_attempts,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-133)    fallback=fallback_llm,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-134)    aggregate_messages=aggregate_messages,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-135)  )
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-136)  return _bind_validator_with_retries(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-137)    bound_llm,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-138)    validator=validator,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-139)    retry_strategy=retry_strategy,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-140)    tool_choice=tool_choice,
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-12-141)  ).with_config(metadata={"retry_strategy": "jsonpatch"})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-13-1)bound_llm = bind_validator_with_jsonpatch_retries(llm, tools=tools)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-14-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-14-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-14-4)  display(Image(bound_llm.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-14-5)except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-14-6)  pass

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-1)chain = prompt | bound_llm
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-2)results = chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-3)  {
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-4)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-5)      (
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-6)        "user",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-7)        f"Extract the summary from the following conversation:\n\n<convo>\n{formatted}\n</convo>",
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-8)      ),
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-9)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-10)  },
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-11))
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-15-12)results.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-3)[{'text': 'Here is a summary of the key points from the conversation:', 'type': 'text'}, {'id': 'toolu_01JjnQVgzPKLCJxXgEppQpfD', 'input': {'key_moments': [{'topic': 'Drake and Kendrick Lamar beef', 'happy_moments': [{'quote': "It's wild how this beef is shaping fans.", 'description': 'The beef is generating a lot of interest and debate among fans.', 'expressed_preference': {'content': 'The beef can push the genre forward and make artists level up.', 'sources': "When it's done right, a beef can push the genre forward and make artists level up."}}, {'quote': 'I just want both of them to keep dropping heat, beef or no beef.', 'description': 'The key is for Drake and Kendrick to keep making great music regardless of their beef.', 'expressed_preference': {'content': 'Wants Drake and Kendrick to keep making great music, beef or no beef.', 'sources': 'I just want both of them to keep dropping heat, beef or no beef.'}}], 'tense_moments': [{'quote': 'Eh', 'description': 'Unclear if the beef is good for hip-hop.', 'expressed_preference': {'content': 'Unsure if the beef is good for hip-hop.', 'sources': 'Eh'}}], 'sad_moments': [{'quote': "Honestly, I think it'll stay a hot topic for the fans, but unless someone drops a straight-up diss track, it's not gonna escalate.", 'description': "The beef may just stay a topic of discussion among fans, but likely won't escalate unless they release direct diss tracks.", 'expressed_preference': {'content': "The beef will likely remain a topic of discussion but won't escalate unless they release diss tracks.", 'sources': "Honestly, I think it'll stay a hot topic for the fans, but unless someone drops a straight-up diss track, it's not gonna escalate."}}], 'background_info': [{'factoid': {'content': "Kendrick's 'Control' verse kicked off the beef.", 'sources': "Definitely was Kendrick's 'Control' verse that kicked it off."}, 'professions': [], 'why': 'This was the event that started the back-and-forth between Drake and Kendrick.'}, {'factoid': {'content': 'Drake never went directly after Kendrick, just some subtle jabs.', 'sources': 'Drake never went after him directly. Just some subtle jabs here and there.'}, 'professions': [], 'why': "Describes the nature of Drake's response to Kendrick's 'Control' verse."}], 'moments_summary': "The conversation covers the ongoing beef between Drake and Kendrick Lamar, including how it started with Kendrick's 'Control' verse, the subtle jabs back and forth, and debate over whether the beef is ultimately good for hip-hop. There are differing views on whether it will escalate beyond just being a topic of discussion among fans."}]}, 'name': 'TranscriptSummary', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-4)Tool Calls:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-5) TranscriptSummary (toolu_017FF4ZMezU4sv87aa8cLjRT)
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-6) Call ID: toolu_017FF4ZMezU4sv87aa8cLjRT
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-7) Args:
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-8)  key_moments: [{'topic': 'Drake and Kendrick Lamar beef', 'happy_moments': [{'quote': "It's wild how this beef is shaping fans.", 'description': 'The beef is generating a lot of interest and debate among fans.', 'expressed_preference': {'content': 'The beef can push the genre forward and make artists level up.', 'sources': "When it's done right, a beef can push the genre forward and make artists level up."}}, {'quote': 'I just want both of them to keep dropping heat, beef or no beef.', 'description': 'The key is for Drake and Kendrick to keep making great music regardless of their beef.', 'expressed_preference': {'content': 'Wants Drake and Kendrick to keep making great music, beef or no beef.', 'sources': 'I just want both of them to keep dropping heat, beef or no beef.'}}], 'tense_moments': [{'quote': 'Eh', 'description': 'Unclear if the beef is good for hip-hop.', 'expressed_preference': {'content': 'Unsure if the beef is good for hip-hop.', 'sources': 'Eh'}}], 'sad_moments': [{'quote': "Honestly, I think it'll stay a hot topic for the fans, but unless someone drops a straight-up diss track, it's not gonna escalate.", 'description': "The beef may just stay a topic of discussion among fans, but likely won't escalate unless they release direct diss tracks.", 'expressed_preference': {'content': "The beef will likely remain a topic of discussion but won't escalate unless they release diss tracks.", 'sources': "Honestly, I think it'll stay a hot topic for the fans, but unless someone drops a straight-up diss track, it's not gonna escalate."}}], 'background_info': [{'factoid': {'content': "Kendrick's 'Control' verse kicked off the beef.", 'sources': "Definitely was Kendrick's 'Control' verse that kicked it off."}, 'professions': [], 'why': 'This was the event that started the back-and-forth between Drake and Kendrick.'}, {'factoid': {'content': 'Drake never went directly after Kendrick, just some subtle jabs.', 'sources': 'Drake never went after him directly. Just some subtle jabs here and there.'}, 'professions': [], 'why': "Describes the nature of Drake's response to Kendrick's 'Control' verse."}], 'moments_summary': "The conversation covers the ongoing beef between Drake and Kendrick Lamar, including how it started with Kendrick's 'Control' verse, the subtle jabs back and forth, and debate over whether the beef is ultimately good for hip-hop. There are differing views on whether it will escalate beyond just being a topic of discussion among fans."}]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-9)  metadata: {'title': 'Drake and Kendrick Beef', 'location': {'sources': 'Conversation transcript', 'content': 'Teleconference'}, 'duration': '25 minutes'}
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-10)  participants: [{'name': {'sources': 'Conversation transcript', 'content': 'Pete'}, 'background_details': []}, {'name': {'sources': 'Conversation transcript', 'content': 'Xu'}, 'background_details': []}, {'name': {'sources': 'Conversation transcript', 'content': 'Laura'}, 'background_details': []}]
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-11)  insightful_quotes: []
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-12)  overall_summary: 
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-13)  next_steps: []
[](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__codelineno-16-14)  other_stuff: []

```


#### And it works![¶](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#and-it-works "Permanent link")

Retries are an easy way to reduce function calling failures. While retrying may become unnecessary with more powerful LLMs, data validation is important to control how LLMs interact with the rest of your software stack.

If you notice high retry rates (using an observability tool like LangSmith), you can set up a rule to send the failure cases to a dataset alongside the corrected values and then automatically program those into your prompts or schemas (or use them as few-shots to have semantically relevant demonstrations).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Competitive Programming  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/) [ Next  Setting up Custom Authentication (Part ⅓)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
