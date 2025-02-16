---
url: https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#how-to-create-map-reduce-branches-for-parallel-execution)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to create map-reduce branches for parallel execution 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/?q= "Share")

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

How-to Guides 
        * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
          * Controllability  Controllability 
            * [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos#controllability)
            * How to create map-reduce branches for parallel execution  [ How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#setup)
            * [ How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/)
            * [ How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
          * [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#setup)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos#controllability)



# How to create map-reduce branches for parallel execution[¶](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#how-to-create-map-reduce-branches-for-parallel-execution "Permanent link")

[Map-reduce](https://en.wikipedia.org/wiki/MapReduce) operations are essential for efficient task decomposition and parallel processing. This approach involves breaking a task into smaller sub-tasks, processing each sub-task in parallel, and aggregating the results across all of the completed sub-tasks. 

Consider this example: given a general topic from the user, generate a list of related subjects, generate a joke for each subject, and select the best joke from the resulting list. In this design pattern, a first node may generate a list of objects (e.g., related subjects) and we want to apply some other node (e.g., generate a joke) to all those objects (e.g., subjects). However, two main challenges arise.

(1) the number of objects (e.g., subjects) may be unknown ahead of time (meaning the number of edges may not be known) when we lay out the graph and (2) the input State to the downstream Node should be different (one for each generated object).

LangGraph addresses these challenges [through its `Send` API](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#send). By utilizing conditional edges, `Send` can distribute different states (e.g., subjects) to multiple instances of a node (e.g., joke generation). Importantly, the sent state can differ from the core graph's state, allowing for flexible and dynamic workflow management. 

![Screenshot 2024-07-12 at 9.45.40 AM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#setup "Permanent link")

This example will require a few dependencies. First, install the LangGraph library, along with the `@langchain/anthropic` package as we'll be using Anthropic LLMs in this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/core

```


Next, set your Anthropic API key:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-1-1)process.env.ANTHROPIC_API_KEY='YOUR_API_KEY'

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-2)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-3)import{StateGraph,END,START,Annotation,Send}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-5)/* Model and prompts */
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-7)// Define model and prompts we will use
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-8)constsubjectsPrompt="Generate a comma separated list of between 2 and 5 examples related to: {topic}."
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-9)constjokePrompt="Generate a joke about {subject}"
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-10)constbestJokePrompt=`Below are a bunch of jokes about {topic}. Select the best one! Return the ID (index) of the best one.
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-12){jokes}`
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-14)// Zod schemas for getting structured output from the LLM
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-15)constSubjects=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-16)subjects:z.array(z.string()),
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-17)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-18)constJoke=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-19)joke:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-20)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-21)constBestJoke=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-22)id:z.number(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-23)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-25)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-26)model:"claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-27)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-29)/* Graph components: define the components that will make up the graph */
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-31)// This will be the overall state of the main graph.
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-32)// It will contain a topic (which we expect the user to provide)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-33)// and then will generate a list of subjects, and then a joke for
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-34)// each subject
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-35)constOverallState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-36)topic:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-37)subjects:Annotation<string[]>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-38)// Notice here we pass a reducer function.
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-39)// This is because we want combine all the jokes we generate
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-40)// from individual nodes back into one list.
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-41)jokes:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-42)reducer:(state,update)=>state.concat(update),
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-43)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-44)bestSelectedJoke:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-45)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-46)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-47)// This will be the state of the node that we will "map" all
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-48)// subjects to in order to generate a joke
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-49)interfaceJokeState{
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-50)subject:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-51)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-52)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-53)// This is the function we will use to generate the subjects of the jokes
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-54)constgenerateTopics=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-55)state:typeofOverallState.State
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-56)):Promise<Partial<typeofOverallState.State>>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-57)constprompt=subjectsPrompt.replace("topic",state.topic);
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-58)constresponse=awaitmodel
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-59).withStructuredOutput(Subjects,{name:"subjects"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-60).invoke(prompt);
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-61)return{subjects:response.subjects};
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-62)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-63)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-64)// Function to generate a joke
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-65)constgenerateJoke=async(state:JokeState):Promise<{jokes:string[]}>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-66)constprompt=jokePrompt.replace("subject",state.subject);
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-67)constresponse=awaitmodel
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-68).withStructuredOutput(Joke,{name:"joke"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-69).invoke(prompt);
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-70)return{jokes:[response.joke]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-71)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-72)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-73)// Here we define the logic to map out over the generated subjects
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-74)// We will use this an edge in the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-75)constcontinueToJokes=(state:typeofOverallState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-76)// We will return a list of `Send` objects
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-77)// Each `Send` object consists of the name of a node in the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-78)// as well as the state to send to that node
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-79)returnstate.subjects.map((subject)=>newSend("generateJoke",{subject}));
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-80)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-81)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-82)// Here we will judge the best joke
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-83)constbestJoke=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-84)state:typeofOverallState.State
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-85)):Promise<Partial<typeofOverallState.State>>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-86)constjokes=state.jokes.join("\n\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-87)constprompt=bestJokePrompt
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-88).replace("jokes",jokes)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-89).replace("topic",state.topic);
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-90)constresponse=awaitmodel
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-91).withStructuredOutput(BestJoke,{name:"best_joke"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-92).invoke(prompt);
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-93)return{bestSelectedJoke:state.jokes[response.id]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-94)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-95)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-96)// Construct the graph: here we put everything together to construct our graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-97)constgraph=newStateGraph(OverallState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-98).addNode("generateTopics",generateTopics)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-99).addNode("generateJoke",generateJoke)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-100).addNode("bestJoke",bestJoke)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-101).addEdge(START,"generateTopics")
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-102).addConditionalEdges("generateTopics",continueToJokes)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-103).addEdge("generateJoke","bestJoke")
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-104).addEdge("bestJoke",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-105)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-2-106)constapp=graph.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-3-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-3-3)constrepresentation=app.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-3-4)constimage=awaitrepresentation.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-3-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-3-7)tslab.display.png(newUint8Array(arrayBuffer));

```


![]()

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-4-1)// Call the graph: here we call it to generate a list of jokes
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-4-2)forawait(constsofawaitapp.stream({topic:"animals"})){
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-4-3)console.log(s);
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-4-4)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-2) generateTopics: { subjects: [ 'lion', 'elephant', 'penguin', 'dolphin' ] }
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-3)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-4){
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-5) generateJoke: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-6)  jokes: [ "Why don't lions like fast food? Because they can't catch it!" ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-7) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-9){
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-10) generateJoke: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-11)  jokes: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-12)   "Why don't elephants use computers? Because they're afraid of the mouse!"
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-13)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-16){
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-17) generateJoke: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-18)  jokes: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-19)   "Why don't dolphins use smartphones? They're afraid of phishing!"
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-20)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-21) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-22)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-23){
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-24) generateJoke: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-25)  jokes: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-26)   "Why don't you see penguins in Britain? Because they're afraid of Wales!"
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-27)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-28) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-29)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-30){
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-31) bestJoke: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-32)  bestSelectedJoke: "Why don't elephants use computers? Because they're afraid of the mouse!"
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-33) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__codelineno-5-34)}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to use LangGraph.js in web environments  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/) [ Next  How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
