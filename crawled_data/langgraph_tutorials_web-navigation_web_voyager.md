---
url: https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#web-voyager)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Web Voyager 

[ ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/?q= "Share")

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
          * Web Voyager  [ Web Voyager  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#setup)
              * [ Install Agent requirements  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#install-agent-requirements)
            * [ Helper File  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#helper-file)
            * [ Define graph  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-graph)
              * [ Define graph state  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-graph-state)
              * [ Define tools  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-tools)
              * [ Define Agent  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-agent)
                * [ Browser Annotations  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#browser-annotations)
                * [ Agent definition  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#agent-definition)
            * [ Compile the graph  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#compile-the-graph)
            * [ Use the graph  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#use-the-graph)
          * [ Competitive Programming  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#setup)
    * [ Install Agent requirements  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#install-agent-requirements)
  * [ Helper File  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#helper-file)
  * [ Define graph  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-graph)
    * [ Define graph state  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-graph-state)
    * [ Define tools  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-tools)
    * [ Define Agent  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-agent)
      * [ Browser Annotations  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#browser-annotations)
      * [ Agent definition  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#agent-definition)
  * [ Compile the graph  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#compile-the-graph)
  * [ Use the graph  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#use-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/web-navigation/web_voyager.ipynb "Edit this page")

# Web Voyager[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#web-voyager "Permanent link")

[WebVoyager](https://arxiv.org/abs/2401.13919) by He, et. al., is a vision-enabled web-browsing agent capable of controlling the mouse and keyboard.

It works by viewing annotated browser screenshots for each turn, then choosing the next step to take. The agent architecture is a basic reasoning and action (ReAct) loop. The unique aspects of this agent are: - It's usage of [Set-of-Marks](https://som-gpt4v.github.io/)-like image annotations to serve as UI affordances for the agent - It's application in the browser by using tools to control both the mouse and keyboard

The overall design looks like the following:

![](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/img/web-voyager.excalidraw.jpg)

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#setup "Permanent link")

First, let's install our required packages:

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-0-2)%pip install -U --quiet langgraph langsmith langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-1)importos
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-2)fromgetpassimport getpass
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-5)def_getpass(env_var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-6)  if not os.environ.get(env_var):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-7)    os.environ[env_var] = getpass(f"{env_var}=")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-1-10)_getpass("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

#### Install Agent requirements[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#install-agent-requirements "Permanent link")

The only additional requirement we have is the [playwright](https://playwright.dev/) browser. Uncomment and install below:

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-2-1)%pip install --upgrade --quiet playwright > /dev/null
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-2-2)!playwright install

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-3-1)importnest_asyncio
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-3-3)# This is just required for running async playwright in a Jupyter notebook
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-3-4)nest_asyncio.apply()

```


## Helper File[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#helper-file "Permanent link")

We will use some JS code for this tutorial, which you should place in a file called `mark_page.js` in the same directory as the notebook you are running this tutorial from.

Show/Hide JS Code

```

  const customCSS = `
    ::-webkit-scrollbar {
      width: 10px;
    }
    ::-webkit-scrollbar-track {
      background: #27272a;
    }
    ::-webkit-scrollbar-thumb {
      background: #888;
      border-radius: 0.375rem;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #555;
    }
  `;
  const styleTag = document.createElement("style");
  styleTag.textContent = customCSS;
  document.head.append(styleTag);
  let labels = [];
  function unmarkPage() {
  // Unmark page logic
  for (const label of labels) {
    document.body.removeChild(label);
  }
  labels = [];
  }
  function markPage() {
  unmarkPage();
  var bodyRect = document.body.getBoundingClientRect();
  var items = Array.prototype.slice
    .call(document.querySelectorAll("*"))
    .map(function (element) {
    var vw = Math.max(
      document.documentElement.clientWidth || 0,
      window.innerWidth || 0
    );
    var vh = Math.max(
      document.documentElement.clientHeight || 0,
      window.innerHeight || 0
    );
    var textualContent = element.textContent.trim().replace(/\s{2,}/g, " ");
    var elementType = element.tagName.toLowerCase();
    var ariaLabel = element.getAttribute("aria-label") || "";
    var rects = [...element.getClientRects()]
      .filter((bb) => {
      var center_x = bb.left + bb.width / 2;
      var center_y = bb.top + bb.height / 2;
      var elAtCenter = document.elementFromPoint(center_x, center_y);
      return elAtCenter === element || element.contains(elAtCenter);
      })
      .map((bb) => {
      const rect = {
        left: Math.max(0, bb.left),
        top: Math.max(0, bb.top),
        right: Math.min(vw, bb.right),
        bottom: Math.min(vh, bb.bottom),
      };
      return {
        ...rect,
        width: rect.right - rect.left,
        height: rect.bottom - rect.top,
      };
      });
    var area = rects.reduce((acc, rect) => acc + rect.width * rect.height, 0);
    return {
      element: element,
      include:
      element.tagName === "INPUT" ||
      element.tagName === "TEXTAREA" ||
      element.tagName === "SELECT" ||
      element.tagName === "BUTTON" ||
      element.tagName === "A" ||
      element.onclick != null ||
      window.getComputedStyle(element).cursor == "pointer" ||
      element.tagName === "IFRAME" ||
      element.tagName === "VIDEO",
      area,
      rects,
      text: textualContent,
      type: elementType,
      ariaLabel: ariaLabel,
    };
    })
    .filter((item) => item.include && item.area >= 20);
  // Only keep inner clickable items
  items = items.filter(
    (x) => !items.some((y) => x.element.contains(y.element) && !(x == y))
  );
  // Function to generate random colors
  function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  // Lets create a floating border on top of these elements that will always be visible
  items.forEach(function (item, index) {
    item.rects.forEach((bbox) => {
    newElement = document.createElement("div");
    var borderColor = getRandomColor();
    newElement.style.outline = `2px dashed ${borderColor}`;
    newElement.style.position = "fixed";
    newElement.style.left = bbox.left + "px";
    newElement.style.top = bbox.top + "px";
    newElement.style.width = bbox.width + "px";
    newElement.style.height = bbox.height + "px";
    newElement.style.pointerEvents = "none";
    newElement.style.boxSizing = "border-box";
    newElement.style.zIndex = 2147483647;
    // newElement.style.background = `${borderColor}80`;
    // Add floating label at the corner
    var label = document.createElement("span");
    label.textContent = index;
    label.style.position = "absolute";
    // These we can tweak if we want
    label.style.top = "-19px";
    label.style.left = "0px";
    label.style.background = borderColor;
    // label.style.background = "black";
    label.style.color = "white";
    label.style.padding = "2px 4px";
    label.style.fontSize = "12px";
    label.style.borderRadius = "2px";
    newElement.appendChild(label);
    document.body.appendChild(newElement);
    labels.push(newElement);
    // item.element.setAttribute("-ai-label", label.textContent);
    });
  });
  const coordinates = items.flatMap((item) =>
    item.rects.map(({ left, top, width, height }) => ({
    x: (left + left + width) / 2,
    y: (top + top + height) / 2,
    type: item.type,
    text: item.text,
    ariaLabel: item.ariaLabel,
    }))
  );
  return coordinates;
  }


```


## Define graph[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-graph "Permanent link")

### Define graph state[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-graph-state "Permanent link")

The state provides the inputs to each node in the graph.

In our case, the agent will track the webpage object (within the browser), annotated images + bounding boxes, the user's initial request, and the messages containing the agent scratchpad, system prompt, and other information.

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-1)fromtypingimport List, Optional
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-4)fromlangchain_core.messagesimport BaseMessage, SystemMessage
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-5)fromplaywright.async_apiimport Page
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-8)classBBox(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-9)  x: float
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-10)  y: float
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-11)  text: str
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-12)  type: str
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-13)  ariaLabel: str
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-16)classPrediction(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-17)  action: str
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-18)  args: Optional[List[str]]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-20)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-21)# This represents the state of the agent
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-22)# as it proceeds through execution
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-23)classAgentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-24)  page: Page # The Playwright web page lets us interact with the web environment
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-25)  input: str # User request
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-26)  img: str # b64 encoded screenshot
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-27)  bboxes: List[BBox] # The bounding boxes from the browser annotation function
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-28)  prediction: Prediction # The Agent's output
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-29)  # A system message (or messages) containing the intermediate steps
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-30)  scratchpad: List[BaseMessage]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-4-31)  observation: str # The most recent response from a tool

```


API Reference: [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html)

### Define tools[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-tools "Permanent link")

The agent has 6 simple tools:

  1. Click (at labeled box)
  2. Type
  3. Scroll
  4. Wait
  5. Go back
  6. Go to search engine (Google)



We define them below here as functions:

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-1)importasyncio
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-2)importplatform
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-5)async defclick(state: AgentState):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-6)  # - Click [Numerical_Label]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-7)  page = state["page"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-8)  click_args = state["prediction"]["args"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-9)  if click_args is None or len(click_args) != 1:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-10)    return f"Failed to click bounding box labeled as number {click_args}"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-11)  bbox_id = click_args[0]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-12)  bbox_id = int(bbox_id)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-13)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-14)    bbox = state["bboxes"][bbox_id]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-15)  except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-16)    return f"Error: no bbox for : {bbox_id}"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-17)  x, y = bbox["x"], bbox["y"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-18)  await page.mouse.click(x, y)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-19)  # TODO: In the paper, they automatically parse any downloaded PDFs
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-20)  # We could add something similar here as well and generally
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-21)  # improve response format.
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-22)  return f"Clicked {bbox_id}"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-23)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-25)async deftype_text(state: AgentState):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-26)  page = state["page"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-27)  type_args = state["prediction"]["args"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-28)  if type_args is None or len(type_args) != 2:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-29)    return (
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-30)      f"Failed to type in element from bounding box labeled as number {type_args}"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-31)    )
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-32)  bbox_id = type_args[0]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-33)  bbox_id = int(bbox_id)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-34)  bbox = state["bboxes"][bbox_id]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-35)  x, y = bbox["x"], bbox["y"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-36)  text_content = type_args[1]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-37)  await page.mouse.click(x, y)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-38)  # Check if MacOS
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-39)  select_all = "Meta+A" if platform.system() == "Darwin" else "Control+A"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-40)  await page.keyboard.press(select_all)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-41)  await page.keyboard.press("Backspace")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-42)  await page.keyboard.type(text_content)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-43)  await page.keyboard.press("Enter")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-44)  return f"Typed {text_content} and submitted"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-45)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-46)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-47)async defscroll(state: AgentState):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-48)  page = state["page"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-49)  scroll_args = state["prediction"]["args"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-50)  if scroll_args is None or len(scroll_args) != 2:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-51)    return "Failed to scroll due to incorrect arguments."
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-52)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-53)  target, direction = scroll_args
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-54)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-55)  if target.upper() == "WINDOW":
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-56)    # Not sure the best value for this:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-57)    scroll_amount = 500
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-58)    scroll_direction = (
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-59)      -scroll_amount if direction.lower() == "up" else scroll_amount
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-60)    )
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-61)    await page.evaluate(f"window.scrollBy(0, {scroll_direction})")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-62)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-63)    # Scrolling within a specific element
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-64)    scroll_amount = 200
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-65)    target_id = int(target)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-66)    bbox = state["bboxes"][target_id]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-67)    x, y = bbox["x"], bbox["y"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-68)    scroll_direction = (
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-69)      -scroll_amount if direction.lower() == "up" else scroll_amount
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-70)    )
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-71)    await page.mouse.move(x, y)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-72)    await page.mouse.wheel(0, scroll_direction)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-73)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-74)  return f"Scrolled {direction} in {'window'iftarget.upper()=='WINDOW'else'element'}"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-75)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-76)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-77)async defwait(state: AgentState):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-78)  sleep_time = 5
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-79)  await asyncio.sleep(sleep_time)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-80)  return f"Waited for {sleep_time}s."
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-81)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-82)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-83)async defgo_back(state: AgentState):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-84)  page = state["page"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-85)  await page.go_back()
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-86)  return f"Navigated back a page to {page.url}."
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-87)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-88)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-89)async defto_google(state: AgentState):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-90)  page = state["page"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-91)  await page.goto("https://www.google.com/")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-5-92)  return "Navigated to google.com."

```


### Define Agent[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#define-agent "Permanent link")

The agent is driven by a multi-modal model and decides the action to take for each step. It is composed of a few runnable objects:

  1. A `mark_page` function to annotate the current page with bounding boxes
  2. A prompt to hold the user question, annotated image, and agent scratchpad
  3. GPT-4V to decide the next steps
  4. Parsing logic to extract the action



Let's first define the annotation step:

#### Browser Annotations[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#browser-annotations "Permanent link")

This function annotates all buttons, inputs, text areas, etc. with numbered bounding boxes. GPT-4V then just has to refer to a bounding box when taking actions, reducing the complexity of the overall task.

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-1)importbase64
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-3)fromlangchain_core.runnablesimport chain as chain_decorator
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-5)# Some javascript we will run on each step
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-6)# to take a screenshot of the page, select the
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-7)# elements to annotate, and add bounding boxes
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-8)with open("mark_page.js") as f:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-9)  mark_page_script = f.read()
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-12)@chain_decorator
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-13)async defmark_page(page):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-14)  await page.evaluate(mark_page_script)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-15)  for _ in range(10):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-16)    try:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-17)      bboxes = await page.evaluate("markPage()")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-18)      break
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-19)    except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-20)      # May be loading...
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-21)      asyncio.sleep(3)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-22)  screenshot = await page.screenshot()
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-23)  # Ensure the bboxes don't follow us around
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-24)  await page.evaluate("unmarkPage()")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-25)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-26)    "img": base64.b64encode(screenshot).decode(),
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-27)    "bboxes": bboxes,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-6-28)  }

```


API Reference: [chain](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.chain.html)

#### Agent definition[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#agent-definition "Permanent link")

Now we'll compose this function with the prompt, llm and output parser to complete our agent.

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-1)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-2)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-3)fromlangchain_core.runnablesimport RunnablePassthrough
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-4)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-7)async defannotate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-8)  marked_page = await mark_page.with_retry().ainvoke(state["page"])
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-9)  return {**state, **marked_page}
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-12)defformat_descriptions(state):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-13)  labels = []
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-14)  for i, bbox in enumerate(state["bboxes"]):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-15)    text = bbox.get("ariaLabel") or ""
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-16)    if not text.strip():
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-17)      text = bbox["text"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-18)    el_type = bbox.get("type")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-19)    labels.append(f'{i} (<{el_type}/>): "{text}"')
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-20)  bbox_descriptions = "\nValid Bounding Boxes:\n" + "\n".join(labels)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-21)  return {**state, "bbox_descriptions": bbox_descriptions}
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-22)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-23)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-24)defparse(text: str) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-25)  action_prefix = "Action: "
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-26)  if not text.strip().split("\n")[-1].startswith(action_prefix):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-27)    return {"action": "retry", "args": f"Could not parse LLM Output: {text}"}
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-28)  action_block = text.strip().split("\n")[-1]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-29)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-30)  action_str = action_block[len(action_prefix) :]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-31)  split_output = action_str.split(" ", 1)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-32)  if len(split_output) == 1:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-33)    action, action_input = split_output[0], None
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-34)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-35)    action, action_input = split_output
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-36)  action = action.strip()
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-37)  if action_input is not None:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-38)    action_input = [
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-39)      inp.strip().strip("[]") for inp in action_input.strip().split(";")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-40)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-41)  return {"action": action, "args": action_input}
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-42)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-43)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-44)# Will need a later version of langchain to pull
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-45)# this image prompt template
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-7-46)prompt = hub.pull("wfh/web-voyager")

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html) | [RunnablePassthrough](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.passthrough.RunnablePassthrough.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-8-1)llm = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=4096)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-8-2)agent = annotate | RunnablePassthrough.assign(
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-8-3)  prediction=format_descriptions | prompt | llm | StrOutputParser() | parse
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-8-4))

```


## Compile the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#compile-the-graph "Permanent link")

We've created most of the important logic. We have one more function to define that will help us update the graph state after a tool is called.

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-1)importre
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-4)defupdate_scratchpad(state: AgentState):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-5)"""After a tool is invoked, we want to update
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-6)  the scratchpad so the agent is aware of its previous steps"""
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-7)  old = state.get("scratchpad")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-8)  if old:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-9)    txt = old[0].content
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-10)    last_line = txt.rsplit("\n", 1)[-1]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-11)    step = int(re.match(r"\d+", last_line).group()) + 1
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-12)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-13)    txt = "Previous action observations:\n"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-14)    step = 1
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-15)  txt += f"\n{step}. {state['observation']}"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-16)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-9-17)  return {**state, "scratchpad": [SystemMessage(content=txt)]}

```


Now we can compose everything into a graph:

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-1)fromlangchain_core.runnablesimport RunnableLambda
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-3)fromlanggraph.graphimport END, START, StateGraph
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-4)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-5)graph_builder = StateGraph(AgentState)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-6)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-8)graph_builder.add_node("agent", agent)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-9)graph_builder.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-11)graph_builder.add_node("update_scratchpad", update_scratchpad)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-12)graph_builder.add_edge("update_scratchpad", "agent")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-14)tools = {
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-15)  "Click": click,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-16)  "Type": type_text,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-17)  "Scroll": scroll,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-18)  "Wait": wait,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-19)  "GoBack": go_back,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-20)  "Google": to_google,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-21)}
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-22)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-23)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-24)for node_name, tool in tools.items():
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-25)  graph_builder.add_node(
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-26)    node_name,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-27)    # The lambda ensures the function's string output is mapped to the "observation"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-28)    # key in the AgentState
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-29)    RunnableLambda(tool) | (lambda observation: {"observation": observation}),
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-30)  )
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-31)  # Always return to the agent (by means of the update-scratchpad node)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-32)  graph_builder.add_edge(node_name, "update_scratchpad")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-33)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-34)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-35)defselect_tool(state: AgentState):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-36)  # Any time the agent completes, this function
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-37)  # is called to route the output to a tool or
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-38)  # to the end user.
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-39)  action = state["prediction"]["action"]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-40)  if action == "ANSWER":
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-41)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-42)  if action == "retry":
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-43)    return "agent"
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-44)  return action
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-45)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-46)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-47)graph_builder.add_conditional_edges("agent", select_tool)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-48)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-10-49)graph = graph_builder.compile()

```


API Reference: [RunnableLambda](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

## Use the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#use-the-graph "Permanent link")

Now that we've created the whole agent executor, we can run it on a few questions! We'll start our browser at "google.com" and then let it control the rest.

Below is a helper function to help print out the steps to the notebook (and display the intermediate screenshots).

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-1)fromIPythonimport display
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-2)fromplaywright.async_apiimport async_playwright
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-4)browser = await async_playwright().start()
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-5)# We will set headless=False so we can watch the agent navigate the web.
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-6)browser = await browser.chromium.launch(headless=False, args=None)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-7)page = await browser.new_page()
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-8)_ = await page.goto("https://www.google.com")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-9)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-10)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-11)async defcall_agent(question: str, page, max_steps: int = 150):
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-12)  event_stream = graph.astream(
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-13)    {
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-14)      "page": page,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-15)      "input": question,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-16)      "scratchpad": [],
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-17)    },
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-18)    {
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-19)      "recursion_limit": max_steps,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-20)    },
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-21)  )
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-22)  final_answer = None
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-23)  steps = []
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-24)  async for event in event_stream:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-25)    # We'll display an event stream here
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-26)    if "agent" not in event:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-27)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-28)    pred = event["agent"].get("prediction") or {}
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-29)    action = pred.get("action")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-30)    action_input = pred.get("args")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-31)    display.clear_output(wait=False)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-32)    steps.append(f"{len(steps)+1}. {action}: {action_input}")
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-33)    print("\n".join(steps))
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-34)    display.display(display.Image(base64.b64decode(event["agent"]["img"])))
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-35)    if "ANSWER" in action:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-36)      final_answer = action_input[0]
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-37)      break
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-11-38)  return final_answer

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-12-1)res = await call_agent("Could you explain the WebVoyager paper (on arxiv)?", page)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-12-2)print(f"Final response: {res}")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-13-1)1. Type: ['7', 'WebVoyager paper arXiv']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-13-2)2. Click: ['32']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-13-3)3. Click: ['3']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-13-4)4. ANSWER;: ['The "WebVoyager" paper discusses the development of an end-to-end web agent that leverages large multimodal models. The abstract highlights the importance of such agents in automating complex tasks on the web, which remains a challenging domain due to the heterogeneity in structure and the semantic gap between humans and machines. The paper proposes a solution that combines neural symbolic models and multimodal web environments, aiming to advance the capabilities of these agents to perform web browsing tasks effectively. Further details would require a more in-depth analysis of the paper\'s content beyond the abstract.']

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-14-1)Final response: The "WebVoyager" paper discusses the development of an end-to-end web agent that leverages large multimodal models. The abstract highlights the importance of such agents in automating complex tasks on the web, which remains a challenging domain due to the heterogeneity in structure and the semantic gap between humans and machines. The paper proposes a solution that combines neural symbolic models and multimodal web environments, aiming to advance the capabilities of these agents to perform web browsing tasks effectively. Further details would require a more in-depth analysis of the paper's content beyond the abstract.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-15-1)res = await call_agent(
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-15-2)  "Please explain the today's XKCD comic for me. Why is it funny?", page
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-15-3))
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-15-4)print(f"Final response: {res}")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-16-1)1. retry: Could not parse LLM Output: I'm sorry, but the image provided does not contain an XKCD comic. The image shows a page from a scientific paper titled "WebVoyager 2: Building an End-to-End Web Agent with Large Multimodal Models." If you provide the XKCD comic you're referring to, I'd be happy to explain the humor in it.
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-16-2)2. retry: Could not parse LLM Output: I'm sorry, but I cannot assist with that request.
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-16-3)3. Google: None
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-16-4)4. Type: ['6', 'xkcd.com']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-16-5)5. Click: ['25']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-16-6)6. ANSWER;: ['The XKCD comic titled "Relationship Advice" pokes fun at the sometimes exaggerated way people talk about the challenges of relationships. It starts with one character stating that relationships require constant work and are like a job, which is a common sentiment. However, the other character takes this comparison to an extreme, calling it a "grueling ordeal" and a "crushing burden," which humorously exaggerates the difficulties of maintaining a relationship. The punchline comes when, after this escalation, the second character insists they\'re fine and that it\'s all normal, which satirizes how people might downplay their struggles to appear in control or deny the extent of their challenges. The humor lies in the hyperbole and the relatable nature of discussing relationship difficulties, as well as the contrast between the characters\' statements and the insistence that everything is okay.']

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-17-1)Final response: The XKCD comic titled "Relationship Advice" pokes fun at the sometimes exaggerated way people talk about the challenges of relationships. It starts with one character stating that relationships require constant work and are like a job, which is a common sentiment. However, the other character takes this comparison to an extreme, calling it a "grueling ordeal" and a "crushing burden," which humorously exaggerates the difficulties of maintaining a relationship. The punchline comes when, after this escalation, the second character insists they're fine and that it's all normal, which satirizes how people might downplay their struggles to appear in control or deny the extent of their challenges. The humor lies in the hyperbole and the relatable nature of discussing relationship difficulties, as well as the contrast between the characters' statements and the insistence that everything is okay.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-18-1)res = await call_agent("What are the latest blog posts from langchain?", page)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-18-2)print(f"Final response: {res}")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-1)1. Google: None
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-2)2. Type: ['6', 'latest blog posts from langchain']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-3)3. Click: ['27']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-4)4. Click: ['14']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-5)5. Click: ['0']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-6)6. retry: Could not parse LLM Output: Thought: The latest blog posts from Langchain are displayed on the right side of the screen with titles and reading time. I will provide the titles of the featured blog posts as seen on the screen.
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-7)
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-8)Action: ANSWER; The latest blog posts from Langchain are:
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-9)1. OpenGPTs - 7 min read
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-10)2. LangGraph: Multi-Agent Workflows - 6 min read
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-11)3. LangGraph - 7 min read
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-12)4. LangChain v0.1.0 - 10 min read
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-19-13)7. ANSWER;: ['The latest blog posts from Langchain are "OpenGPTs," "LangGraph: Multi-Agent Workflows," and "LangGraph."']

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-20-1)Final response: The latest blog posts from Langchain are "OpenGPTs," "LangGraph: Multi-Agent Workflows," and "LangGraph."

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-21-1)res = await call_agent(
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-21-2)  "Could you check google maps to see when i should leave to get to SFO by 7 o'clock? starting from SF downtown.",
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-21-3)  page,
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-21-4))
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-21-5)print(f"Final response: {res}")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-1)1. Google: None
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-2)2. Type: ['6', 'Google Maps']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-3)3. Click: ['0']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-4)4. Click: ['0']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-5)5. Wait: None
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-6)6. Click: ['22']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-7)7. Click: ['0']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-8)8. Click: ['2']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-9)9. Type: ['0', 'San Francisco downtown to SFO']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-10)10. Click: ['1']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-11)11. Click: ['2']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-12)12. Type: ['8', 'San Francisco International Airport SFO']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-13)13. Click: ['14']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-14)14. Click: ['28']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-15)15. Scroll: ['WINDOW', 'up']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-16)16. Scroll: ['WINDOW', 'up']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-17)17. Click: ['10']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-18)18. Click: ['28']
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-22-19)19. ANSWER;: ['To arrive at San Francisco International Airport (SFO) by 7:00 AM starting from downtown San Francisco, you should leave by 6:46 AM according to the current Google Maps information, which estimates a 44-minute travel time.']

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__codelineno-23-1)Final response: To arrive at San Francisco International Airport (SFO) by 7:00 AM starting from downtown San Francisco, you should leave by 6:46 AM according to the current Google Maps information, which estimates a 44-minute travel time.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  TNT-LLM: Text Mining at Scale  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/) [ Next  Competitive Programming  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
