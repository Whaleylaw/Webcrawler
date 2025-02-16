---
url: https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#competitive-programming)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Competitive Programming 

[ ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/?q= "Share")

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
          * Competitive Programming  [ Competitive Programming  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#setup)
              * [ Data  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#data)
              * [ Test Evaluation Utils  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#test-evaluation-utils)
            * [ Part 1: Zero-Shot with Reflection  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-1-zero-shot-with-reflection)
              * [ State  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#state)
                * [ Node 1: Solver  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-1-solver)
                * [ Node 2: Evaluate  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-2-evaluate)
                * [ Create Graph  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#create-graph)
            * [ Part 2: Few-shot Retrieval  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-2-few-shot-retrieval)
              * [ State  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#state_1)
              * [ Nodes 1 and 3: Draft & Solver  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#nodes-1-and-3-draft-solver)
              * [ Node 2: Retrieve  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-2-retrieve)
              * [ Graph  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#graph)
            * [ Part 3: Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-3-human-in-the-loop)
            * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#conclusion)
          * [ Complex data extraction with function calling  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#setup)
    * [ Data  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#data)
    * [ Test Evaluation Utils  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#test-evaluation-utils)
  * [ Part 1: Zero-Shot with Reflection  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-1-zero-shot-with-reflection)
    * [ State  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#state)
      * [ Node 1: Solver  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-1-solver)
      * [ Node 2: Evaluate  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-2-evaluate)
      * [ Create Graph  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#create-graph)
  * [ Part 2: Few-shot Retrieval  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-2-few-shot-retrieval)
    * [ State  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#state_1)
    * [ Nodes 1 and 3: Draft & Solver  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#nodes-1-and-3-draft-solver)
    * [ Node 2: Retrieve  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-2-retrieve)
    * [ Graph  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#graph)
  * [ Part 3: Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-3-human-in-the-loop)
  * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#conclusion)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/usaco/usaco.ipynb "Edit this page")

# Competitive Programming[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#competitive-programming "Permanent link")

In this tutorial, you will build a computing olympiad agent that leverages three complementary techniques to boost performance: **reflection** , **retrieval** , and **human-in-the-loop** collaboration. These techniques and data are all adapted from the paper "Can Language Models Solve Olympiad Programming?" by Quan Shi, Michael Tang, Karthik Narasimhan, and Shunyu Yao. You can check out their paper at the following link:

[![arXiv](http://img.shields.io/badge/cs.CL-arXiv%3A2404.10952v1-B31B1B.svg)](https://arxiv.org/abs/2404.10952v1)

You will construct an agentic graph capable of answering programming questions of increasing difficulty.

  1. **Reflection** : In part 1, you will create a zero-shot tool calling agent and prompt it to reflect on the test case results to correct its initial errors. This is similar to the agent the paper reported as having a pass rate of 12.38 on the USACO benchmark.
  2. **Retrieval** : In Part 2, you will implement an initial retrieval step as "episodic memory" for the agent that retrieves high-quality few-shot examples from our corpora of programming problems to help solve the **bronze** level question. This agent is similar to the one the paper benchmarked at 20.2.
  3. **Human-in-the-loop** : In part 3, you will use `interrupt_after` to let the user copilot the agent to a better answer. The benchmark performance then is constrained only by the competitiveness of the human it is paired with.



Your final agent graph will be structured like the diagram below:

![](https://langchain-ai.github.io/langgraph/tutorials/usaco/img/diagram.png)

Parts 1 and 2 are analogous to the systems benchmarked in the paper as having a pass rate of 12.38 and 20.2 respectively.

![Benchmark system results]()

While LLMs are not yet capable of autonomously solving all these problems, we can design the system that far surpasses the capabilities of a basic ReAct agent at answering these questions. 

Before diving in, let's set up our machine. This will involve installing dependencies, fetching the dataset, and defining a utility function.

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#setup "Permanent link")

For this tutorial, we will need to install some dependencies, fetch the Olympiad dataset, and define a utility function to help run the candidate solutions to see if they pass the test cases.

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-0-2)%pip install -U langgraph langsmith langchain_anthropic datasets langchain langchainhub

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-5)def_get_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-1-10)_get_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

#### Data[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#data "Permanent link")

Fetch the USACO benchmark data using the util below:

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-1)importos
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-2)importzipfile
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-4)importdatasets
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-5)importrequests
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-7)usaco_url = "https://storage.googleapis.com/benchmarks-artifacts/usaco/usaco_sampled_with_tests.zip"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-8)zip_path = "usaco.zip"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-9)extract_path = "usaco_datasets"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-11)response = requests.get(usaco_url)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-12)with open(zip_path, "wb") as file:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-13)  file.write(response.content)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-14)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-15)with zipfile.ZipFile(zip_path, "r") as zip_ref:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-16)  zip_ref.extractall(extract_path)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-18)os.remove(zip_path)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-2-20)ds = datasets.load_from_disk(os.path.join(extract_path, "usaco_v3_sampled_with_tests"))

```


#### Test Evaluation Utils[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#test-evaluation-utils "Permanent link")

We also need a way to evaluate our generated code. We will use this unsafe code execution program to run the generated code against our test cases. **Note:** The code below runs arbitrary code on your local machine! Proceed with caution.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-1)importmultiprocessing
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-2)importqueue
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-3)importsubprocess
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-4)importsys
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-5)importtime
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-6)importtraceback
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-8)multiprocessing.set_start_method("fork", force=True)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-9)# WARNING
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-10)# This program exists to execute untrusted model-generated code. Although
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-11)# it is highly unlikely that model-generated code will do something overtly
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-12)# malicious in response to this test suite, model-generated code may act
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-13)# destructively due to a lack of model capability or alignment.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-14)# Users are strongly encouraged to sandbox this evaluation suite so that it
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-15)# does not perform destructive actions on their host or network.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-16)# Proceed at your own risk:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-19)defexec_program(q, program, input_data, expected_output, timeout):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-20)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-21)    start_time = time.time()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-22)    process = subprocess.Popen(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-23)      [sys.executable, "-c", program],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-24)      stdin=subprocess.PIPE,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-25)      stdout=subprocess.PIPE,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-26)      stderr=subprocess.PIPE,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-27)      text=True,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-28)    )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-29)    stdout, stderr = process.communicate(input=input_data, timeout=timeout)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-30)    if time.time() - start_time > timeout:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-31)      raise TimeoutError("Execution timed out.")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-32)    if process.returncode != 0:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-33)      q.put(f"failed: {stderr}")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-34)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-35)      if stdout.strip() == expected_output.strip():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-36)        q.put("passed")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-37)      else:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-38)        q.put(f"wrong answer. Expected '{expected_output}', got '{stdout}'")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-39)  except subprocess.TimeoutExpired:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-40)    process.kill()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-41)    q.put("timed out")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-42)  except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-43)    q.put(f"failed: {traceback.format_exc()}")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-44)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-45)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-46)defcheck_correctness(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-47)  program: str, input_data: str, expected_output: str, timeout: float
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-48)) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-49)  q = multiprocessing.Queue()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-50)  process = multiprocessing.Process(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-51)    target=exec_program, args=(q, program, input_data, expected_output, timeout)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-52)  )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-53)  process.start()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-54)  process.join(timeout=timeout + 1)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-55)  if process.is_alive():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-56)    process.terminate()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-57)    process.join()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-58)    result = "timed out"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-59)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-60)    try:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-61)      result = q.get_nowait()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-62)    except queue.Empty:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-63)      result = "no result returned"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-3-64)  return result

```


Let's check an example program and output to see how it works:

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-1)program_code = "print('hello, world!')"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-2)input_data = ""
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-3)expected_output = "hello, world!"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-4)timeout = 2
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-6)test_result = check_correctness(program_code, input_data, expected_output, timeout)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-7)print("Example 1: ", test_result)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-8)test_result = check_correctness("print('goodbye')", input_data, "hi there", timeout)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-4-9)print("Example 2: ", test_result)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-5-1)Example 1: passed
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-5-2)Example 2: wrong answer. Expected 'hi there', got 'goodbye
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-5-3)'

```


## Part 1: Zero-Shot with Reflection[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-1-zero-shot-with-reflection "Permanent link")

In our first section, we will build a simple zero-shot tool-calling agent to try to solve these problems. We will incorporate a simple form of [reflection](https://www.youtube.com/watch?v=v5ymBTXNqtk) directly in the agent's tool calling schema by adding a "reasoning" field. Furthermore, Claude was trained to "reason" with freeform text prior to invoking any tools. Together, this should induce reflective "chain-of-thought" prompting.

_Note: this diverges somewhat from the paper's implementation, which uses an explicit reflection step with a variation of the[Reflexion](https://langchain-ai.github.io/langgraph/tutorials/reflexion/reflexion) prompt._

By the end of this section, we will have built a reflective zero-shot programming agent that looks like the section marked "Part 1" in the system diagram below:

![](https://langchain-ai.github.io/langgraph/tutorials/usaco/img/diagram-part-1.png)

### State[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#state "Permanent link")

LangGraph's main primitive is the `StateGraph`, which you use to define an agent as a controllable state machine. The graph has `node`'s (python functions) that perform the work, and `edge`s that define how to route between the nodes. The `State` defines the interface between each node and carries all the information your agent needs.

Below, define a `State` for our programming olympiad agent. The `messages` will track the sequence of submissions (and test case feedback) as chat history. The `status` field will flip from `in_progress` to `success` if the submission passes all test cases. The other fields (test_cases, runtime_limit) are used by the `evaluation` node to test the agent's submissions. These values are not seen by the agent itself.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-5)fromlanggraph.graph.messageimport AnyMessage, add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-8)classTestCase(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-9)  inputs: str
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-10)  outputs: str
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-13)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-14)  # Append-only chat memory so the agent can try to recover from initial mistakes.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-15)  messages: Annotated[list[AnyMessage], add_messages]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-16)  # From the dataset. These are used for testing.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-17)  test_cases: list[TestCase]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-18)  runtime_limit: int
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-6-19)  status: str

```


API Reference: [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

Now, convert the dataset into inputs our graph will accept.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-1)input_states = [
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-3)    "messages": [("user", row["description"])],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-4)    "test_cases": row["test_cases"],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-5)    "runtime_limit": row["runtime_limit"],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-6)    "status": "in_progress",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-7)    "problem_level": row["problem_level"],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-8)  }
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-9)  for row in ds
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-7-10)]

```


#### Node 1: Solver[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-1-solver "Permanent link")

Create a `solver` node that prompts an LLM "agent" to use a [writePython tool](https://python.langchain.com/docs/integrations/chat/anthropic/#integration-details) to generate the submitted code.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-1)fromlangchain_core.language_modelsimport BaseChatModel
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-2)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-4)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-7)classwritePython(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-8)"""Write python code that resolves the problem."""
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-10)  reasoning: str = Field(..., description="Conceptual solution.")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-11)  pseudocode: str = Field(..., description="Detailed English pseudocode.")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-12)  code: str = Field(..., description="Valid Python 3 solution to the problem")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-14)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-15)classSolver:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-16)  def__init__(self, llm: BaseChatModel, prompt: ChatPromptTemplate):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-17)    self.runnable = prompt | llm.bind_tools([writePython])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-19)  def__call__(self, state: State) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-20)    # Our agent only can see the "messages" and will ignore the test info
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-8-21)    return {"messages": [self.runnable.invoke({"messages": state["messages"]})]}

```


API Reference: [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)

Now, create the solver below. We'll use Claude Opus

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-1)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-2)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-4)# For this section, we are testing zero-shot performance and won't have
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-5)# any examples. Partial them out to pre-fill the template.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-6)prompt = hub.pull("wfh/usaco-draft-solver").partial(examples="")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-7)print("*" * 35 + "Prompt" + "*" * 35)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-8)prompt.pretty_print()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-10)# Use Haiku if you want to save $$ while (almost) never correctly answering the question
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-11)# llm = ChatAnthropic(model="claude-3-haiku-20240307")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-12)llm = ChatAnthropic(model="claude-3-opus-20240229")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-13)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-9-14)solver = Solver(llm, prompt)

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-1)***********************************Prompt***********************************
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-2)================================[1m System Message [0m================================
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-4)You are a world-class competitive programmer.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-5)Please reply with a Python 3 solution to the problem below. 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-6)First, reason through the problem and conceptualize a solution.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-7)Then write detailed pseudocode to uncover any potential logical errors or omissions.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-8)Finally output the working Python code for your solution, ensuring to fix any errors uncovered while writing pseudocode.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-10)No outside libraries are allowed.[33;1m[1;3m{examples}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-12)=============================[1m Messages Placeholder [0m=============================
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-10-14)[33;1m[1;3m{messages}[0m

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-1)print("*" * 34 + " Example " + "*" * 34)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-2)result = solver(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-3)  {
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-4)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-5)      (
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-6)        "user",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-7)        "How do I get a perfectly random sample from an infinite stream",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-8)      )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-9)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-10)  }
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-11))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-12)result["messages"][0].pretty_print()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-13)# Could expand to include (1)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-14)# 1. Restate the problem in plain English
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-15)# 2. Closely following the explanation, restate and explain the solution in plain English
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-16)# 3. Write a pseudocode solution
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-11-17)# 4. Output the final Python solution with your solution steps in comments.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-12-1)********************************** Example **********************************
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-12-2)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-12-4)[{'text': "<thinking>\nTo address this problem, we need to use the writePython function, which requires the following parameters:\n- reasoning: a conceptual solution to the problem\n- pseudocode: detailed pseudocode for the solution\n- code: working Python code implementing the solution\n\nThe key aspects to address in the solution are:\n1. We have an infinite stream, so we can't store all elements. Need an online algorithm.\n2. Need to ensure each element has an equal probability of being in the final sample.\n\nI believe I have enough information to provide values for all the required parameters.\n</thinking>", 'type': 'text'}, {'id': 'toolu_01UqpLYyueky5GtYMidS9oLF', 'input': {'reasoning': 'To get a perfectly random sample of size k from an infinite stream:\n\n1. Store the first k elements in an array (reservoir). \n2. For each ith element after the kth element (i > k):\n  - Generate a random integer j between 0 and i (inclusive)\n  - If j < k, replace the jth element of the reservoir with the ith element\n3. At the end, the reservoir contains the random sample.\n\nThis works because for any element, when we process the nth element, the probability that it is in the reservoir is:\n- k/n when n <= k (first k elements always selected)\n- k/n * k/(n-1) * k/(n-2) * ... * k/(k+1) = k/n when n > k\n\nSo any element has k/n probability of being in final reservoir, giving a perfectly random sample.', 'pseudocode': '\`\`\`\nfunction selectKItems(stream, k):\n  reservoir = [0..k-1] # store first k elements\n\n  i = k\n  while stream has next item:\n    item = stream.next()\n    j = random(0, i) # generate random index between 0 and i\n    if j < k:\n      reservoir[j] = item # replace element at random index with new item\n    i += 1\n\n  return reservoir\n\`\`\`', 'code': 'import random\n\ndef reservoir_sampling(stream, k):\n  reservoir = []\n  \n  # Store first k elements in reservoir\n  for i in range(k):\n    reservoir.append(next(stream))\n\n  i = k\n  for item in stream:\n    # Generate random index between 0 and i\n    j = random.randint(0, i) \n    \n    # Replace element at random index with new item\n    if j < k:\n      reservoir[j] = item\n    i += 1\n\n  return reservoir'}, 'name': 'writePython', 'type': 'tool_use'}]

```


#### Node 2: Evaluate[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-2-evaluate "Permanent link")

Now define the "`evaluate`" node. This node takes the `solver`'s submitted code and executes it against the `test_cases` in our `State`. This uses the unsafe `check_correctness` utility we defined in the setup above.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-1)fromlangchain_core.messagesimport AIMessage, HumanMessage, ToolMessage
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-4)# This is the node we will add to the graph.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-5)# Most tool-calling APIs require that the `ToolMessage` contain the ID
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-6)# of the
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-7)defformat_tool_message(response: str, ai_message: AIMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-8)  return ToolMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-9)    content=response + "\nMake all fixes using the writePython tool.",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-10)    tool_call_id=ai_message.tool_calls[0]["id"],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-11)  )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-12)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-13)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-14)defevaluate(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-15)  test_cases = state["test_cases"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-16)  ai_message: AIMessage = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-17)  if not ai_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-18)    return {
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-19)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-20)        HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-21)          content="No code submitted. Please try again using the correct python code."
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-22)        )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-23)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-24)    }
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-25)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-26)    code = ai_message.tool_calls[0]["args"]["code"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-27)  except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-28)    return {"messages": [format_tool_message(repr(e), ai_message)]}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-29)  num_test_cases = len(test_cases)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-30)  succeeded = 0
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-31)  test_results = []
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-32)  # TODO: Multiprocess
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-33)  for test_case in test_cases:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-34)    input_data = test_case["inputs"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-35)    expected_output = test_case["outputs"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-36)    test_result = check_correctness(code, input_data, expected_output, timeout)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-37)    test_results.append(test_result)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-38)    if test_result == "passed":
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-39)      succeeded += 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-40)  pass_rate = succeeded / num_test_cases if num_test_cases else "N/A"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-41)  if pass_rate == 1:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-42)    return {"status": "success"}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-43)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-44)  responses = "\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-45)    [f"<test id={i}>\n{r}\n</test>" for i, r in enumerate(test_results)]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-46)  )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-47)  response = f"Incorrect submission. Please respond with updated code.\nPass rate: {succeeded}/{num_test_cases}\nResults:\n{responses}"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-48)  formatted_message = format_tool_message(response, ai_message)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-13-49)  return {"messages": [formatted_message]}

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html)

#### Create Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#create-graph "Permanent link")

Now, put it all together! Once you've defined each node, defining the connectivity / state transitions is fairly easy.

Our Zero-shot graph defines a loop. If we visualize the data flow, we want the logic to: 1. First go to the `solver`, which attempts a first solution. 2. Next go to the `evaluate` node, which tests the solution. 3. If the solution passes, end, otherwise, return to the `solver` to try again.

In LangGraph, we use `conditional_edges` to define state transitions that contain conditional logic. Below, define the graph, adding a `control_edge` to handle step (3) above.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-3)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-4)builder.add_node("solver", solver)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-5)builder.add_edge(START, "solver")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-6)builder.add_node("evaluate", evaluate)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-7)builder.add_edge("solver", "evaluate")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-9)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-10)defcontrol_edge(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-11)  if state.get("status") == "success":
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-12)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-13)  return "solver"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-14)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-15)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-16)builder.add_conditional_edges("evaluate", control_edge, {END: END, "solver": "solver"})
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-14-17)graph = builder.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-15-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-15-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-15-4)  display(Image(graph.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-15-5)except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-15-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-15-7)  pass

```


![]()

Now that we've created our graph, let's see the type of question it will have to solve.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-16-1)input_state = input_states[0].copy()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-16-2)# We will reduce the test cases to speed this notebook up
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-16-3)input_state["test_cases"] = input_state["test_cases"][:3]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-16-4)print(input_state["messages"][0][1])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-1)Farmer John has $N$ ($1 \leq N \leq 2 \cdot 10^5$) farms, numbered from $1$ to
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-2)$N$. It is known that FJ closes farm $i$ at time $c_i$. Bessie wakes up at time
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-3)$S$, and wants to maximize the productivity of her day by visiting as many farms
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-4)as possible before they close. She plans to visit farm $i$ on time $t_i + S$.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-5)Bessie must arrive at a farm strictly before Farmer John closes it to actually visit it.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-6)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-7)Bessie has $Q$ $(1 \leq Q \leq 2 \cdot 10^5)$ queries. For each query, she gives
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-8)you two integers $S$ and $V$. For each query, output whether Bessie can visit at
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-9)least $V$ farms if she wakes up at time $S$.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-10)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-11)INPUT FORMAT (input arrives from the terminal / stdin):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-12)The first line consists of $N$ and $Q$.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-13)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-14)The second line consists of $c_1, c_2, c_3 \dots c_N$ ($1 \leq c_i \leq 10^6$).
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-15)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-16)The third line consists of $t_1, t_2, t_3 \dots t_N$ ($1 \leq t_i \leq 10^6$).
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-17)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-18)The next $Q$ lines each consist of two integers $V$ ($1 \leq V \leq N$) and $S$
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-19)($1 \leq S \leq 10^6$).
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-20)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-21)OUTPUT FORMAT (print output to the terminal / stdout):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-22)For each of the $Q$ queries, output YES or NO on a new line.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-23)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-24)SAMPLE INPUT:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-25)5 5
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-26)3 5 7 9 12
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-27)4 2 3 3 8
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-28)1 5
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-29)1 6
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-30)3 3
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-31)4 2
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-32)5 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-33)SAMPLE OUTPUT: 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-34)YES
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-35)NO
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-36)YES
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-37)YES
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-38)NO
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-39)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-40)For the first query, Bessie will visit the farms at time $t = [9, 7, 8, 8, 13]$,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-41)so she will only get to visit farm $4$ on time before FJ closes the farm.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-42)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-43)For the second query, Bessie will not be able to visit any of the farms on time.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-44)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-45)For the third query, Bessie will visit farms $3, 4, 5$ on time.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-46)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-47)For the fourth and fifth queries, Bessie will be able to visit all but the first
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-48)farm on time.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-49)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-50)SCORING:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-51)Inputs 2-4: $N,Q\le 10^3$Inputs 5-9: $c_i, t_i \le 20$Inputs 10-17: No additional constraints.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-52)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-53)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-17-54)Problem credits: Chongtian Ma

```


Pretty difficult! Let's run our simple "zero-shot" agent below to see how it fares. **It most likely will not be able to solve this question** (unless you are using a more powerful model than what I had available at the time of writing this tutorial (2024/04/20). We will trace the trajectory to LangSmith to review the series of submissions. To reduce the packet size, we will use "`hide_inputs`" and filter out the test_cases. All this is optional but useful for development. 

**Note:** We _expect_ a **GraphRecursionError** here from it not being able to answer it correctly in the allocated number of steps.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-1)fromlangchain_core.tracers.contextimport tracing_v2_enabled
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-2)fromlangsmithimport Client
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-5)# We don't need to include all the test cases in our traces.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-6)def_hide_test_cases(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-7)  copied = inputs.copy()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-8)  # These are tens of MB in size. No need to send them up
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-9)  copied["test_cases"] = "..."
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-10)  return copied
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-11)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-12)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-13)client = Client(hide_inputs=_hide_test_cases, hide_outputs=_hide_test_cases)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-14)with tracing_v2_enabled(client=client):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-15)  events = graph.stream(input_state)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-16)  for event in events:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-17)    for value in event.values():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-18)      messages = value.get("messages")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-19)      if messages:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-20)        if isinstance(messages, list):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-21)          messages = value["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-22)        print(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-23)          "Assistant:",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-24)          str(messages.content).replace("\n", "\\n")[:50],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-18-25)        )

```


API Reference: [tracing_v2_enabled](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.context.tracing_v2_enabled.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-1)Assistant: [{'text': '<thinking>\nThe key steps to solve this
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-2)Assistant: KeyError('code')\nMake all fixes using the writePy
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-3)Assistant: [{'id': 'toolu_01KimhKt8aqQjGZJmrHVnAtE', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-4)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-5)Assistant: [{'id': 'toolu_01CMZTqAd7BZQ2nSgtk9djRW', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-6)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-7)Assistant: [{'id': 'toolu_01Kbaq9gX4BnHvps6TMfVGHL', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-8)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-9)Assistant: [{'id': 'toolu_01MiSnpiGK5Yy4Cpp6GGbjmT', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-10)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-11)Assistant: [{'id': 'toolu_01GWuvJezXLMVurUBG84odDP', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-12)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-13)Assistant: [{'id': 'toolu_01W8DGmhcpFVctySmx58scf9', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-14)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-15)Assistant: [{'id': 'toolu_018bhYtCKDK6S4MHiAxUZCrb', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-16)Assistant: KeyError('code')\nMake all fixes using the writePy
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-17)Assistant: [{'id': 'toolu_01LCwaCjX9uZBV3jt9eAkmAa', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-18)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-19)Assistant: [{'id': 'toolu_01WqJvdE2WDeTZXoKp2V7PWb', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-20)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-21)Assistant: [{'id': 'toolu_01DGevkunt9zWx7SVDCHdBuv', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-22)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-23)Assistant: [{'id': 'toolu_013comYKVxNSzTM4ZbH3L3FP', 'input':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-19-24)Assistant: Incorrect submission. Please respond with updated

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-1)---------------------------------------------------------------------------
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-2)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-3)GraphRecursionError            Traceback (most recent call last)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-4)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-5)Cell In[25], line 17
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-6)   15 with tracing_v2_enabled(client=client):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-7)   16   events = graph.stream(input_state)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-8)---> 17   for event in events:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-9)   18     for value in event.values():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-10)   19       messages = value.get("messages")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-11)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-12)File ~/.pyenv/versions/3.11.2/lib/python3.11/site-packages/langgraph/pregel/__init__.py:645, in Pregel.stream(self, input, config, stream_mode, output_keys, input_keys, interrupt_before_nodes, interrupt_after_nodes, debug)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-13)  643     break
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-14)  644 elif step == config["recursion_limit"]:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-15)--> 645   raise GraphRecursionError(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-16)  646     f"Recursion limit of {config['recursion_limit']} reached"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-17)  647     "without hitting a stop condition. You can increase the "
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-18)  648     "limit by setting the `recursion_limit` config key."
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-19)  649   )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-20)  651 # before execution, check if we should interrupt
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-21)  652 if _should_interrupt(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-22)  653   checkpoint,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-23)  654   interrupt_before_nodes,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-24)  655   self.stream_channels_list,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-25)  656   next_tasks,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-26)  657 ):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-27)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-20-28)GraphRecursionError: Recursion limit of 25 reachedwithout hitting a stop condition. You can increase the limit by setting the `recursion_limit` config key.

```


It wasn't able to solve it in time **but that's OK**! If it were easy, this paper would be a lot shorter :)

You can view the [agent's full LangSmith trace](https://smith.langchain.com/public/61c84ad0-51db-40f1-b50d-6983d9481ca1/r) at the provided link.

In the next section we will add an improvement the paper terms "episodic memory", which in this case is really few-shot retrieval.

## Part 2: Few-shot Retrieval[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-2-few-shot-retrieval "Permanent link")

Even with reflective tool calling, our baseline agent from part 1 struggled with this difficult task. One way to "teach" an LLM how to better perform a task is through demonstrations, also known as "few-shot examples."

What the authors of the USACO paper call "episodic memory" **is really just few-shot prompting over similar examples.**

Each examples in this case is a different problems + solution within the dataset. The term "episodic memory" makes sense if you pretend your agent has already "solved" these problems and is recalling its solutions to them.

This section adds the "Episodic Memory" components from "Part 2" in the diagram below.

![](https://langchain-ai.github.io/langgraph/tutorials/usaco/img/diagram-part-2.png)

Note that this memory step is performed **one time** , **before** the logic of our zero-shot loop from part 1. The steps are as follows:

  1. Prompt the LLM to generate a candidate solution.
  2. Use the text of the candidate solution to retrieve the N most similar (problem, solution) pairs.
  3. Format this result in the Zero-shot agent's prompt.



Below, let's implement our episodic memory as a retriever. We will follow the paper's retriever selection and use [BM25](https://en.wikipedia.org/wiki/Okapi_BM25).

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-21-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-21-2)%pip install --upgrade --quiet rank_bm25

```


#### State[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#state_1 "Permanent link")

The state is mostly recycled from part 1. Add additional "candidate" and "examples" fields to store the information for the memory steps.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-5)fromlanggraph.graph.messageimport AnyMessage, add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-6)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-7)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-8)classTestCase(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-9)  inputs: str
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-10)  outputs: str
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-11)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-12)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-13)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-14)  # NEW! Candidate for retrieval + formatted fetched examples as "memory"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-15)  candidate: AIMessage
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-16)  examples: str
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-17)  # Repeated from Part 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-18)  messages: Annotated[list[AnyMessage], add_messages]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-19)  test_cases: list[TestCase]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-20)  runtime_limit: int
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-22-21)  status: str

```


API Reference: [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

#### Nodes 1 and 3: Draft & Solver[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#nodes-1-and-3-draft-solver "Permanent link")

Let's create our "agent". We will modify the `Solver` from Part 1 to reuse it for for the agent node and for the candidate program generation node ("draft").

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-1)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-2)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-5)classSolver:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-6)  def__init__(self, llm: BaseChatModel, prompt: ChatPromptTemplate):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-7)    self.runnable = prompt | llm.bind_tools([writePython])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-9)  def__call__(self, state: State) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-10)    # Our agent only can see the "messages" and will ignore the test info
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-11)    inputs = {"messages": state["messages"]}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-12)    has_examples = bool(state.get("examples"))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-13)    output_key = "candidate" # Used in the draft node
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-14)    if has_examples:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-15)      output_key = "messages"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-16)      # Used in the solve node
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-17)      inputs["examples"] = state["examples"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-18)    response = self.runnable.invoke(inputs)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-19)    if not response.content:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-20)      return {
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-21)        output_key: AIMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-22)          content="I'll need to think about this step by step."
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-23)        )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-24)      }
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-25)    return {output_key: response}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-26)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-27)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-28)prompt = hub.pull("wfh/usaco-draft-solver")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-29)llm = ChatAnthropic(model="claude-3-opus-20240229")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-30)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-31)draft_solver = Solver(llm, prompt.partial(examples=""))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-23-32)solver = Solver(llm, prompt)

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html)

#### Node 2: Retrieve[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#node-2-retrieve "Permanent link")

The retrieve node takes a candidate solution (made by the 'solver' node), uses _this_ to search for similar examples, then formats those in the message.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-24-1)# We will test our agent on index 0 (the same as above).
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-24-2)# Later, we will test on index 2 (the first 'silver difficulty' question)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-24-3)test_indices = [0, 2]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-24-4)train_ds = [row for i, row in enumerate(ds) if i not in test_indices]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-24-5)test_ds = [row for i, row in enumerate(ds) if i in test_indices]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-1)fromlangchain_community.retrieversimport BM25Retriever
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-4)defformat_example(row):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-5)  question = row["description"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-6)  answer = row["solution"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-7)  return f"""<problem>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-8){question}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-9)</problem>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-10)<solution>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-11){answer}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-12)</solution>"""
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-13)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-14)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-15)# Skip our 'test examples' to avoid cheating
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-16)# This is "simulating" having seen other in-context examples
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-25-17)retriever = BM25Retriever.from_texts([format_example(row) for row in train_ds])

```


API Reference: [BM25Retriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.bm25.BM25Retriever.html)

Now define the node. Any node can optionally accept a second `config` positional argument. This contains `configurable` params you can adjust when invoking the graph. For instance, we can adjust the top `k` examples to retrieve for our agent.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-1)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-4)defretrieve_examples(state: State, config: RunnableConfig):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-5)  top_k = config["configurable"].get("k") or 2
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-6)  ai_message: AIMessage = state["candidate"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-7)  if not ai_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-8)    # We err here. To make more robust, you could loop back
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-9)    raise ValueError("Draft agent did not produce a valid code block")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-10)  code = ai_message.tool_calls[0]["args"]["code"]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-11)  examples_str = "\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-12)    [doc.page_content for doc in retriever.invoke(code)[:top_k]]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-13)  )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-14)  examples_str = f"""
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-15)You previously solved the following problems in this competition:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-16)<Examples>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-17){examples_str}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-18)<Examples>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-19)Approach this new question with similar sophistication."""
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-26-20)  return {"examples": examples_str}

```


API Reference: [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

#### Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#graph "Permanent link")

Now let's put it all together. The graph is slightly more complicated than in part 1, since we have to add the initial "draft" and "retrieve" nodes to our agent loop.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-2)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-4)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-5)builder.add_node("draft", draft_solver)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-6)builder.add_edge(START, "draft")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-7)builder.add_node("retrieve", retrieve_examples)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-8)builder.add_node("solve", solver)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-9)builder.add_node("evaluate", evaluate)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-10)# Add connectivity
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-11)builder.add_edge("draft", "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-12)builder.add_edge("retrieve", "solve")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-13)builder.add_edge("solve", "evaluate")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-14)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-15)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-16)defcontrol_edge(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-17)  if state.get("status") == "success":
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-18)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-19)  return "solve"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-20)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-21)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-22)builder.add_conditional_edges("evaluate", control_edge, {END: END, "solve": "solve"})
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-23)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-24)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-25)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-27-26)graph = builder.compile(checkpointer=checkpointer)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-28-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-28-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-28-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-28-4)  display(Image(graph.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-28-5)except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-28-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-28-7)  pass

```


![]()

Let's try again on this problem:

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-1)config = {"configurable": {"thread_id": "question-recall", "k": 3}}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-2)with tracing_v2_enabled(client=client):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-3)  events = graph.stream(input_state, config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-4)  for event in events:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-5)    for value in event.values():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-6)      messages = value.get("messages")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-7)      if messages:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-8)        if isinstance(messages, list):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-9)          messages = value["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-10)        print(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-11)          "Assistant:",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-12)          str(messages.content).replace("\n", "\\n")[:50],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-13)        )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-14)      elif value.get("examples"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-15)        print("Retrieved examples:\n\n", value["examples"][:100] + "...")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-16)      elif value.get("candidate"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-29-17)        print(str(value["candidate"].content)[:200])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-1)[{'text': "<thinking>\nThis problem essentially asks to find the number of farms Bessie can visit before they close at each query. The key insights are:\n\n1. Bessie's arrival time at each farm is S +
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-2)Retrieved examples:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-5)You previously solved the following problems in this competition:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-6)<Examples>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-7)<problem>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-9)Farmer John...
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-30-10)Assistant: [{'text': "<thinking>\nThe key information given i

```


**No recursion error!** You can view the [full LangSmith trace](https://smith.langchain.com/public/1f1c4db3-b53c-49bf-a287-a2b51c081156/r/31f90ddd-8ae9-4b23-a2b5-b0c0d67c5cc3) of the graph's execution at the provided link to confirm the results. You can also check the graph state to confirm that it passed all test cases successfully: 

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-31-1)checkpoint = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-31-2)checkpoint.values["status"]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-32-1)'success'

```


**Congrats!** You added "episodic memory" to your agent to fetch few-shot examples and solve this bronze level programming olympiad question!

Our agent is still limited, however. Let's test it out on a more challenging 🪙🏆silver✨ level question:

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-33-1)silver_row = test_ds[1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-33-2)silver_row["problem_level"]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-34-1)'silver'

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-1)silver_input = {
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-2)  "messages": [("user", silver_row["description"])],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-3)  "test_cases": silver_row["test_cases"],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-4)  "runtime_limit": silver_row["runtime_limit"],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-5)  "status": "in_progress",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-6)}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-7)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-9)config = {"configurable": {"thread_id": "silver-question-1", "k": 2}}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-10)with tracing_v2_enabled(client=client):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-11)  events = graph.stream(silver_input, config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-12)  for event in events:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-13)    for value in event.values():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-14)      messages = value.get("messages")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-15)      if messages:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-16)        if isinstance(messages, list):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-17)          messages = value["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-18)        print(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-19)          "Assistant:",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-20)          str(messages.content).replace("\n", "\\n")[:50],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-21)        )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-22)      elif value.get("examples"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-23)        print("Retrieved examples:\n\n", value["examples"][:100] + "...")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-24)      elif value.get("candidate"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-35-25)        print(str(value["candidate"].content)[:200])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-1)[{'text': "<thinking>\nThe relevant tool for this problem is writePython. It requires the following parameters:\n- reasoning: To solve this problem, we need to simulate the cruise by following the seq
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-2)Retrieved examples:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-5)You previously solved the following problems in this competition:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-6)<Examples>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-7)<problem>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-9)Farmer John...
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-10)Assistant: [{'text': "<thinking>\nTo solve this problem, we n
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-11)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-12)Assistant: [{'text': "<thinking>\nAfter reviewing the failed 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-13)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-14)Assistant: [{'text': "<thinking>\nAfter reviewing the latest 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-15)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-16)Assistant: [{'text': "<thinking>\nOops, looks like I made a s
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-17)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-18)Assistant: [{'text': "<thinking>\nHmm, some of the test cases
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-19)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-20)Assistant: [{'text': '<thinking>\nOops, looks like I accident
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-21)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-22)Assistant: [{'text': "<thinking>\nLooks like the code is now 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-23)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-24)Assistant: [{'text': '<thinking>\nOops, looks like I accident
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-25)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-26)Assistant: [{'text': "<thinking>\nHmm, the optimization to si
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-27)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-28)Assistant: [{'text': "<thinking>\nOops, I did it again - acci
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-29)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-30)Assistant: [{'text': "<thinking>\nHmm, the latest code is sti
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-36-31)Assistant: Incorrect submission. Please respond with updated

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-1)---------------------------------------------------------------------------
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-2)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-3)GraphRecursionError            Traceback (most recent call last)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-4)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-5)Cell In[37], line 12
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-6)   10 with tracing_v2_enabled(client=client):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-7)   11   events = graph.stream(silver_input, config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-8)---> 12   for event in events:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-9)   13     for value in event.values():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-10)   14       messages = value.get("messages")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-11)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-12)File ~/.pyenv/versions/3.11.2/lib/python3.11/site-packages/langgraph/pregel/__init__.py:645, in Pregel.stream(self, input, config, stream_mode, output_keys, input_keys, interrupt_before_nodes, interrupt_after_nodes, debug)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-13)  643     break
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-14)  644 elif step == config["recursion_limit"]:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-15)--> 645   raise GraphRecursionError(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-16)  646     f"Recursion limit of {config['recursion_limit']} reached"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-17)  647     "without hitting a stop condition. You can increase the "
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-18)  648     "limit by setting the `recursion_limit` config key."
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-19)  649   )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-20)  651 # before execution, check if we should interrupt
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-21)  652 if _should_interrupt(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-22)  653   checkpoint,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-23)  654   interrupt_before_nodes,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-24)  655   self.stream_channels_list,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-25)  656   next_tasks,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-26)  657 ):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-27)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-37-28)GraphRecursionError: Recursion limit of 25 reachedwithout hitting a stop condition. You can increase the limit by setting the `recursion_limit` config key.

```


**Still too hard!** AGI not achieved yet. To investigate our agent's trajectory in detail, check out the [full LangSmith trace](https://smith.langchain.com/public/13018b44-0c4f-4f1a-9e6d-dea1f3fd4705/r).

Our agent isn't good enough to be autonomous. The great thing about LangGraph is you don't have to decide between "autonomous agent" and "simple DAG": you can inject control and user-interfaces wherever it can usefully benefit your application.

## Part 3: Human-in-the-loop[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#part-3-human-in-the-loop "Permanent link")

Our retrieval-enhanced agent was able to solve the `bronze`-level question but still failed for those with the more challenging **silver** difficulty. 

Recall that the paper presented 3 complementary techniques that improved performance:

  1. Reflection: explicitly prompting the LLM to "reflect" on its mistakes can help it
  2. Few-shot prompting: retrieving relevant, high-quality examples as "memory"
  3. **Human-in-the-loop collaboration:** without giving the correct answer, the human is allowed to help the agent reflect on its approach and point it in a better direction.



In this section, we will add the "human" node (marked as "part 3" in the diagram below), completing our agent graph:

![](https://langchain-ai.github.io/langgraph/tutorials/usaco/img/diagram.png)

From an ML perspective, this is a bit of a [clever hans](https://en.wikipedia.org/wiki/Clever_Hans), but from the application designer's perspective, where the primary goal is to achieve a higher combined success rate, letting the human interject with thoughts and insights is only natural. 

In either case, adding a human check to a LangGraph instance requires no extra lines of code. Let's do so by instructing the graph to `interrupt_after` the "`evaluate`" node to give the user a chance to modify the trajectory.

Start assembling your graph below. The following section is identical to our application in part 2:

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-1)# This is all the same as before
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-2)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-3)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-5)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-6)prompt = hub.pull("wfh/usaco-draft-solver")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-7)llm = ChatAnthropic(model="claude-3-opus-20240229", max_tokens_to_sample=4000)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-9)draft_solver = Solver(llm, prompt.partial(examples=""))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-10)builder.add_node("draft", draft_solver)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-11)builder.add_edge(START, "draft")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-12)builder.add_node("retrieve", retrieve_examples)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-13)solver = Solver(llm, prompt)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-14)builder.add_node("solve", solver)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-15)builder.add_node("evaluate", evaluate)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-16)builder.add_edge("draft", "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-17)builder.add_edge("retrieve", "solve")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-18)builder.add_edge("solve", "evaluate")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-19)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-20)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-21)defcontrol_edge(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-22)  if state.get("status") == "success":
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-23)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-24)  return "solve"
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-25)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-26)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-27)builder.add_conditional_edges("evaluate", control_edge, {END: END, "solve": "solve"})
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-38-28)checkpointer = MemorySaver()

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

Now finish by compiling the graph. Set`interrupt_after=["evaluate"]` to instruct the agent to wait for human input before continuing execution.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-39-1)graph = builder.compile(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-39-2)  checkpointer=checkpointer,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-39-3)  # New: this tells the graph to break any time it goes to the "human" node
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-39-4)  interrupt_after=["evaluate"],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-39-5))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-40-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-40-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-40-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-40-4)  display(Image(graph.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-40-5)except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-40-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-40-7)  pass

```


![]()

As you can see in the graph above, the structure is the same as Part 2, except that we've inserted a "`human`" breakpoint between the "`evaluate`" and "`solve`" nodes.

Let's try this question again!

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-1)config = {"configurable": {"thread_id": "silver-hl-1", "k": 2}}
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-2)with tracing_v2_enabled(client=client):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-3)  events = graph.stream(silver_input, config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-4)  for event in events:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-5)    for value in event.values():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-6)      messages = value.get("messages")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-7)      if messages:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-8)        if isinstance(messages, list):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-9)          messages = value["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-10)        print(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-11)          "Assistant:",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-12)          str(messages.content).replace("\n", "\\n")[:50],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-13)        )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-14)      elif value.get("examples"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-15)        print("Retrieved examples:\n\n", value["examples"][:100] + "...")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-16)      elif value.get("candidate"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-41-17)        print(str(value["candidate"].content)[:200])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-1)[{'text': "<thinking>\nTo solve this problem, we need to:\n1. Read in the input data - number of ports N, length of direction sequence M, number of repetitions K, the port connections, and the directi
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-2)Retrieved examples:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-4)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-5)You previously solved the following problems in this competition:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-6)<Examples>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-7)<problem>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-8)Farmer John ...
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-9)Assistant: [{'text': '<thinking>\nTo determine where Bessie e
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-42-10)Assistant: Incorrect submission. Please respond with updated

```


**⏰Time to weigh in⏰:** our model failed in its first attempt, so we have the opportunity to give it some advice. 

Recall the original question:

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-43-1)snapshot = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-43-2)print(snapshot.values["messages"][0].content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-1)Problem 3: Luxury River Cruise [Josh Alman and Nathan Pinsker, 2013]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-3)Farmer John is taking Bessie and the cows on a cruise! They are sailing on a 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-4)network of rivers with N ports (1 <= N <= 1,000) labeled 1..N, and Bessie 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-5)starts at port 1. Each port has exactly two rivers leading out of it which 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-6)lead directly to other ports, and rivers can only be sailed one way.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-7)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-8)At each port, the tour guides choose either the "left" river or the "right" 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-9)river to sail down next, but they keep repeating the same choices over and 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-10)over. More specifically, the tour guides have chosen a short sequence of M 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-11)directions (1 <= M <= 500), each either "left" or "right", and have
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-12)repeated it K times (1 <= K <= 1,000,000,000). Bessie thinks she is going
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-13)in circles -- help her figure out where she ends up!
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-14)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-15)PROBLEM NAME: cruise
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-16)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-17)INPUT FORMAT:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-18)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-19)* Line 1: Three space-separated integers N, M, and K.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-20)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-21)* Lines 2..N+1: Line i+1 has two space-separated integers,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-22)    representing the number of the ports that port i's left and
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-23)    right rivers lead to, respectively.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-24)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-25)* Line N+2: M space-separated characters, either 'L' or 'R'. 'L'
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-26)    represents a choice of 'left' and 'R' represents a choice of
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-27)    'right'.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-28)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-29)SAMPLE INPUT:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-30)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-31)4 3 3
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-32)2 4
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-33)3 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-34)4 2
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-35)1 3
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-36)L L R
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-37)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-38)INPUT DETAILS:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-39)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-40)The port numbers are arranged clockwise in a circle, with 'L' being a 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-41)clockwise rotation and 'R' being a counterclockwise rotation. The sequence 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-42)taken is LLRLLRLLR.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-43)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-44)OUTPUT FORMAT:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-45)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-46)* Line 1: A single integer giving the number of the port where
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-47)    Bessie's cruise ends.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-48)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-49)SAMPLE OUTPUT:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-50)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-51)4
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-52)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-53)OUTPUT DETAILS:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-54)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-55)After the first iteration of the sequence of directions, Bessie is at port
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-56)2 (1 -> 2 -> 3 -> 2); after the second, she is at port 3 (2 -> 3 -> 4 ->
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-44-57)3), and at the end she is at port 4 (3 -> 4 -> 1 -> 4).

```


And then review the agent's current submission: 

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-45-1)snapshot = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-45-2)print(snapshot.values["messages"][-2].content[0]["text"])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-45-3)print("\n\nCode:\n\n")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-45-4)print(snapshot.values["messages"][-2].tool_calls[0]["args"]["code"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-1)<thinking>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-2)To determine where Bessie ends up, we need to:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-3)1. Simulate the cruise by following the sequence of left/right directions
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-4)2. Repeat this sequence K times to find the final destination port
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-5)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-6)The problem provides:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-7)- The number of ports N
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-8)- The connections between ports (left and right rivers for each port)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-9)- The sequence of M directions (L or R) to follow
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-10)- The number of times K to repeat the sequence
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-11)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-12)With this information, we have everything needed to simulate the cruise and find the ending port. The key steps will be:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-13)1. Read in the input data to initialize the river connections and direction sequence 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-14)2. Iterate K times:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-15)  - For each direction in the M-length sequence:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-16)   - Move to the next port based on the current port and direction 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-17)3. Output the final port number after K iterations
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-18)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-19)The solution will require loops to repeat the sequence K times and follow the M directions. Since K can be up to 1 billion, simulating all K iterations directly would be too slow. Instead, we can find a pattern in how the port changes after each M-length sequence, and then "fast-forward" by calculating which port we reach after K repetitions of the pattern.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-20)</thinking>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-21)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-22)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-23)Code:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-24)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-25)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-26)N, M, K = map(int, input().split())
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-27)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-28)ports = []
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-29)for _ in range(N):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-30) left, right = map(int, input().split())
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-31) ports.append((left, right))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-32)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-33)directions = input().split()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-34)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-35)cur = 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-36)pattern = []
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-37)seen = set() 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-38)steps = 0
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-39)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-40)while cur not in seen:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-41) seen.add(cur)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-42) for d in directions:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-43)  steps += 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-44)  if d == 'L': 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-45)   cur = ports[cur-1][0]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-46)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-47)   cur = ports[cur-1][1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-48) pattern.append((cur, steps))
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-49)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-50)K %= steps
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-51)for port, step in pattern:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-52) if step > K:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-53)  cur = port
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-54)  break
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-55) K -= step
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-56)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-46-57)print(cur)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-47-1)print(snapshot.values["messages"][-1].content[:200])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-1)Incorrect submission. Please respond with updated code.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-2)Pass rate: 4/10
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-3)Results:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-4)<test id=0>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-5)wrong answer. Expected '4
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-6)', got '3
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-7)'
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-8)</test>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-9)<test id=1>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-10)wrong answer. Expected '50
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-11)', got '2
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-12)'
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-13)</test>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-48-14)<t

```


The agent failed. It's on the right track but clearly doesn't handle all the edge cases. 

The agent needs to remember that simulation should include the cycle + whatever steps led up to the example. It could use the "tortoise and hare" algo for cycle detection, use the simulated path and break if and when a repeat is detected, and then 

Let's let the agent know this by **updating the graph state**.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-1)updated_config = graph.update_state(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-2)  config,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-3)  values={
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-4)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-5)      (
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-6)        "user",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-7)"""Consider breaking down the algorithm into separate parts: reading inputs, detecting cycles using the tortoise and hare algorithm, and determining Bessie's final position by skipping ahead K steps.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-9)Read the inputs into three arrays:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-10)- Two arrays L and R for the ports (adjust for 0-based indexing)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-11)- A third array S for the direction sequence
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-12)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-13)Optimize by multiplying K by M before the main loop to convert the number of repetitions into the total number of steps.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-14)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-15)Use the tortoise and hare algorithm to detect the cycle:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-16)- Define a helper function get_next(v) that returns the next position and direction index
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-17)- Initialize two pointers s0 and s1 to (0, 0)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-18)- In each iteration:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-19) - Move s0 by 1 step and s1 by 2 steps using get_next()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-20) - If s0 equals s1, decrement K by 1 and break out of the loop
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-21) - Otherwise, decrement K by 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-22)- After the loop, if K is not 0, there is a cycle
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-23)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-24)To find the cycle length:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-25)- Initialize a counter variable rho to 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-26)- Move s0 by 1 step using get_next()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-27)- Enter a loop:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-28) - Move s0 by 1 step using get_next()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-29) - Increment rho
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-30) - If s0 equals s1, break out of the loop
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-31)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-32)Skip ahead by reducing K modulo rho.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-33)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-34)Simulate the remaining steps:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-35)- While K > 0, move s0 to the next position using get_next() and decrement K
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-36)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-37)Print the final position (converted to 1-based indexing).
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-38)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-39)Pay close attention to the initialization and movement of pointers during cycle detection and length calculation. Ensure that the logic is correct and handles all cases accurately.""",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-40)      )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-41)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-42)  },
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-49-43))

```


Now the graph's state contains our new message.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-50-1)graph.get_state(config).values["messages"][-1]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-51-1)HumanMessage(content="Consider breaking down the algorithm into separate parts: reading inputs, detecting cycles using the tortoise and hare algorithm, and determining Bessie's final position by skipping ahead K steps.\n\nRead the inputs into three arrays:\n- Two arrays L and R for the ports (adjust for 0-based indexing)\n- A third array S for the direction sequence\n\nOptimize by multiplying K by M before the main loop to convert the number of repetitions into the total number of steps.\n\nUse the tortoise and hare algorithm to detect the cycle:\n- Define a helper function get_next(v) that returns the next position and direction index\n- Initialize two pointers s0 and s1 to (0, 0)\n- In each iteration:\n - Move s0 by 1 step and s1 by 2 steps using get_next()\n - If s0 equals s1, decrement K by 1 and break out of the loop\n - Otherwise, decrement K by 1\n- After the loop, if K is not 0, there is a cycle\n\nTo find the cycle length:\n- Initialize a counter variable rho to 1\n- Move s0 by 1 step using get_next()\n- Enter a loop:\n - Move s0 by 1 step using get_next()\n - Increment rho\n - If s0 equals s1, break out of the loop\n\nSkip ahead by reducing K modulo rho.\n\nSimulate the remaining steps:\n- While K > 0, move s0 to the next position using get_next() and decrement K\n\nPrint the final position (converted to 1-based indexing).\n\nPay close attention to the initialization and movement of pointers during cycle detection and length calculation. Ensure that the logic is correct and handles all cases accurately.", id='98888982-a469-4c5a-ab65-743d2f2608dc')

```


Let's let the agent try again. Call `stream` with `None` to just use the inputs loaded from the memory. We will skip our human review for the next few attempats to see if it can correct itself.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-1)num_trials = 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-2)with tracing_v2_enabled(client=client):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-3)  for _ in range(num_trials):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-4)    events = graph.stream(None, updated_config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-5)    for event in events:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-6)      for value in event.values():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-7)        messages = value.get("messages")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-8)        if messages:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-9)          if isinstance(messages, list):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-10)            messages = value["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-11)          print(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-12)            "Assistant:",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-13)            str(messages.content).replace("\n", "\\n")[:50],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-14)          )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-15)        elif value.get("examples"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-16)          print("Retrieved examples:\n\n", value["examples"][:100] + "...")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-17)        elif value.get("candidate"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-18)          print(str(value["candidate"].content)[:200])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-19)    if graph.get_state(config).values["status"] == "success":
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-20)      break
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-52-21)    print("Continuing...")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-53-1)Assistant: [{'text': '<thinking>\nThank you for the detailed 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-53-2)Assistant: Incorrect submission. Please respond with updated 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-53-3)Continuing...

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-54-1)most_recent_state = list(graph.get_state_history(config))[0]

```


OK so the agent tried again. Check out the [LangSmith trace](https://smith.langchain.com/public/707be522-9eaf-4b6a-994e-1742f421a433/r/add3d8e7-85b1-40cf-bbd3-e78c50f835e8) from this step to see its update.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-55-1)snapshot = graph.get_state(most_recent_state.config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-55-2)ai_message = snapshot.values["messages"][-2]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-55-3)if ai_message.content:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-55-4)  print(ai_message.content)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-55-5)print("\n\nCode:\n\n")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-55-6)print(ai_message.tool_calls[0]["args"]["code"] if ai_message.tool_calls else "N/A")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-1)[{'text': '<thinking>\nThank you for the detailed algorithm breakdown! Let me go through each step to make sure I understand and have the necessary information to implement the solution.\n\nReading inputs:\n- Read N, M, K and store in separate variables\n- Create arrays L and R to store the left and right port connections (adjust for 0-based indexing)\n- Create array S to store the M-length direction sequence \n- Multiply K by M upfront to get the total number of steps\n\nDetecting cycles with tortoise and hare:\n- Define get_next(v) to return the next position and direction index\n - It will use the current position and direction to look up the next port in L/R\n- Initialize two pointers s0 and s1 to (0, 0) \n- Loop until s0 equals s1 or all K steps are taken:\n - Move s0 by 1 step and s1 by 2 steps using get_next()\n - Decrement K\n- After the loop, check if K is 0 to determine if a cycle was found\n\nFinding cycle length:\n- If a cycle was found, initialize rho to 1\n- Move s0 by 1 step \n- Loop until s0 equals s1 again:\n - Move s0 by 1 step and increment rho\n- rho will equal the cycle length\n\nSkipping ahead:\n- Reduce K by taking it modulo rho\n\nSimulating remaining steps:\n- While K is greater than 0:\n - Move s0 using get_next()\n - Decrement K\n- s0 will hold the final position\n\nPrinting result:\n- Add 1 to the final position to convert back to 1-based indexing before printing\n\nThe key aspects are:\n- Handling the input format and 0-based indexing \n- Defining get_next() to handle moving to the next port based on direction\n- Correctly implementing the tortoise and hare cycle detection\n- Finding the cycle length after detection\n- Skipping ahead with modulo and simulating any remaining steps\n- Adjusting the output back to 1-based indexing\n\nI believe I have all the necessary pieces to implement this solution now. Let me code it up using the writePython tool.\n</thinking>', 'type': 'text'}, {'id': 'toolu_01EDrYeHJU7GxApRb1QfMA1b', 'input': {'reasoning': "Here's the problem-solving approach:\n\n1. Read in the input data:\n  - N ports, M-length direction sequence, K repetitions\n  - L and R arrays for left/right port connections\n  - S array for direction sequence\n  - Multiply K by M to get total steps\n\n2. Define get_next(v) helper function:\n  - Takes current position and direction index\n  - Returns next position and incremented direction index\n  - Looks up next port in L/R arrays based on current direction\n\n3. Detect cycle using tortoise and hare algorithm:\n  - Initialize s0 and s1 pointers to (0, 0)\n  - Loop until match or all steps taken:\n   - Move s0 by 1 step, s1 by 2 steps\n   - Decrement K\n  - Check if K is 0 after loop\n\n4. If cycle found, find cycle length:\n  - Initialize rho to 1\n  - Move s0 by 1 step\n  - Loop until s0 equals s1 again:\n   - Move s0 and increment rho\n  - rho is the cycle length\n\n5. Skip ahead by K % rho steps\n\n6. Simulate remaining steps:\n  - While K > 0:\n   - Move s0 with get_next()\n   - Decrement K\n  \n7. Print final position (+1 for 1-based indexing)\n\nKey points:\n- Multiplying K*M avoids nested loop\n- get_next() handles port transitions \n- Tortoise and hare finds cycles\n- Modulo skips ahead in cycle\n- Adjust 0-based indexing for input/output", 'pseudocode': "1. Read input:\n  N, M, K = read_ints()\n  L = [0] * N\n  R = [0] * N\n  for i in 0..N-1:\n   L[i], R[i] = read_ints()\n  S = read_direction_sequence()\n  K *= M\n\n2. Define get_next(v):\n  def get_next(pos, dir_idx):\n   if S[dir_idx] == 'L':\n    next_pos = L[pos]\n   else:\n    next_pos = R[pos]\n   next_dir_idx = (dir_idx + 1) % M\n   return (next_pos, next_dir_idx)\n\n3. Find cycle:\n  s0 = (0, 0)\n  s1 = (0, 0) \n  while K:\n   s0 = get_next(s0[0], s0[1])\n   s1 = get_next(s1[0], get_next(s1[0], s1[1])[1])\n   K -= 1\n   if s0 == s1: break\n  if K != 0: no cycle, print s0[0] + 1\n\n4. Find cycle length:\n  rho = 1\n  s0 = get_next(s0[0], s0[1])\n  while s0 != s1:\n   s0 = get_next(s0[0], s0[1]) \n   rho += 1\n\n5. Skip steps:\n  K %= rho\n\n6. Remaining steps: \n  while K:\n   s0 = get_next(s0[0], s0[1])\n   K -= 1\n   \n7. Print result:\n  print(s0[0] + 1)", 'code': "def read_ints():\n return map(int, input().split())\n\nN, M, K = read_ints()\n\nL = [0] * N\nR = [0] * N\nfor i in range(N):\n L[i], R[i] = read_ints()\n L[i] -= 1\n R[i] -= 1\n\nS = input().split()\n\nK *= M\n\ndef get_next(pos, dir_idx):\n if S[dir_idx] == 'L':\n  next_pos = L[pos] \n else:\n  next_pos = R[pos]\n next_dir_idx = (dir_idx + 1) % M\n return (next_pos, next_dir_idx)\n\ns0 = (0, 0) \ns1 = (0, 0)\n\nwhile K:\n if s0 == s1: break\n \n s0 = get_next(s0[0], s0[1])\n s1 = get_next(s1[0], get_next(s1[0], s1[1])[1])\n \n K -= 1\n \nif K:\n rho = 1\n s0 = get_next(s0[0], s0[1])\n while s0 != s1:\n  s0 = get_next(s0[0], s0[1])\n  rho += 1\n \n K %= rho\n \nwhile K: \n s0 = get_next(s0[0], s0[1])\n K -= 1\n \nprint(s0[0] + 1)"}, 'name': 'writePython', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-2)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-3)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-4)Code:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-5)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-6)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-7)def read_ints():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-8) return map(int, input().split())
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-9)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-10)N, M, K = read_ints()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-11)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-12)L = [0] * N
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-13)R = [0] * N
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-14)for i in range(N):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-15) L[i], R[i] = read_ints()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-16) L[i] -= 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-17) R[i] -= 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-18)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-19)S = input().split()
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-20)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-21)K *= M
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-22)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-23)def get_next(pos, dir_idx):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-24) if S[dir_idx] == 'L':
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-25)  next_pos = L[pos] 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-26) else:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-27)  next_pos = R[pos]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-28) next_dir_idx = (dir_idx + 1) % M
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-29) return (next_pos, next_dir_idx)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-30)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-31)s0 = (0, 0) 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-32)s1 = (0, 0)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-33)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-34)while K:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-35) if s0 == s1: break
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-36)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-37) s0 = get_next(s0[0], s0[1])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-38) s1 = get_next(s1[0], get_next(s1[0], s1[1])[1])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-39)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-40) K -= 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-41)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-42)if K:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-43) rho = 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-44) s0 = get_next(s0[0], s0[1])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-45) while s0 != s1:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-46)  s0 = get_next(s0[0], s0[1])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-47)  rho += 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-48)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-49) K %= rho
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-50)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-51)while K: 
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-52) s0 = get_next(s0[0], s0[1])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-53) K -= 1
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-54)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-56-55)print(s0[0] + 1)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-57-1)print(snapshot.values["messages"][-1].content[:200])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-1)Incorrect submission. Please respond with updated code.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-2)Pass rate: 3/10
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-3)Results:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-4)<test id=0>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-5)passed
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-6)</test>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-7)<test id=1>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-8)timed out
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-9)</test>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-10)<test id=2>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-11)timed out
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-12)</test>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-13)<test id=3>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-14)timed out
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-15)</test>
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-58-16)<t

```


Still getting most test cases wrong. 

Let's provide more feedback.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-1)updated_config = graph.update_state(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-2)  updated_config,
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-3)  values={
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-4)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-5)      (
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-6)        "user",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-7)"""That's better, but you're still getting some errors. Let's double check some things:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-8)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-9)1. When calculating the cycle length, make sure the initialization and movement of the pointers is correct. Double-check the logic there and see if you can spot any discrepancies.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-10)2. Check the condition for whether there's a cycle after the main loop to ensure it covers all cases, like if K becomes 0 in the last iteration.
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-11)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-12)Think step by step through youur implementation and update using the writePython tool.""",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-13)      )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-14)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-15)  },
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-59-16))

```


Now that we've provided this feedback, let's give the agent a few attempts at solving it before we weigh in again.

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-1)num_trials = 2
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-2)with tracing_v2_enabled(client=client):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-3)  for _ in range(num_trials):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-4)    events = graph.stream(None, updated_config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-5)    for event in events:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-6)      for value in event.values():
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-7)        messages = value.get("messages")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-8)        if messages:
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-9)          if isinstance(messages, list):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-10)            messages = value["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-11)          print(
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-12)            "Assistant:",
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-13)            str(messages.content).replace("\n", "\\n")[:50],
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-14)          )
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-15)        elif value.get("examples"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-16)          print("Retrieved examples:\n\n", value["examples"][:100] + "...")
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-17)        elif value.get("candidate"):
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-18)          print(str(value["candidate"].content)[:200])
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-19)    if graph.get_state(config).values["status"] == "success":
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-20)      break
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-60-21)    print("Continuing...")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-61-1)Assistant: [{'text': "<thinking>\nThe algorithm looks mostly

```


You can review [a LangSmith trace (link)](https://smith.langchain.com/public/d383e743-f8f1-4206-9dce-47627f152612/r/3f89582f-9107-461a-a34e-608d52641eeb) of the agent's response to your feedback at the provided link. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-62-1)snapshot = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-62-2)print(snapshot.values["status"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__codelineno-63-1)success

```


**Success!** - the LLM really wouldn't have been able to come to the correct answer without detailed human involvement. 

## Conclusion[¶](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#conclusion "Permanent link")

Congrats on making it to the end! In this tutorial, you implemented an agent in LangGraph capable of solving challenging programming problems. You did so by leveraging a few common techniques to improve performance, including:

  1. **Reflection** : while we didn't implement an explicit reflection step, our prompt and tool invocation was designed to encourage critique of previous outputs. You added this in Part 1.
  2. **Retrieval** : the "episodic memory" of the agent retrieves high-quality few-shot examples from our corpora of programming problems to help solve the **bronze** level question. In Part 2, you implemented a retrieval memory as an initial step.
  3. **Human-in-the-loop** : LLM-powered agents are still too weak to answer all these questions autonomously, but at times, they can get most of the way there and land on the right answer with human feedback. In Part 3, you used `interrupt_after` on the `evaluate` node and then included your feedback by using `update_state` on the graph.



LLMs are not capable of solving all these problems autonomously, but through better prompting and clever engineering, you can create a system that is able to more reliably arrive at the proper solution.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Web Voyager  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/) [ Next  Complex data extraction with function calling  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
