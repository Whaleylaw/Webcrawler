---
url: https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#how-to-install-and-manage-dependencies)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to install and manage dependencies 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/?q= "Share")

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
        * Installation  Installation 
          * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)
          * How to install and manage dependencies  [ How to install and manage dependencies  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/) Table of contents 
            * [ Next steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#next-steps)
          * [ How to use LangGraph.js in web environments  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/)
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
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

  * [ Next steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#next-steps)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)



# How to install and manage dependencies[¶](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#how-to-install-and-manage-dependencies "Permanent link")

LangGraph.js is part of the [LangChain](https://js.langchain.com/) ecosystem, which includes the primary `langchain`[](https://www.npmjs.com/package/langchain) package as well as packages that contain integrations with individual third-party providers. They can be as specific as `@langchain/anthropic`[](https://www.npmjs.com/package/@langchain/anthropic), which contains integrations just for Anthropic chat models, or as broad as `@langchain/community`[](https://www.npmjs.com/package/@langchain/community), which contains broader variety of community contributed integrations.

These packages, as well as LangGraph.js itself, all rely on `@langchain/core`[](https://www.npmjs.com/package/@langchain/core), which contains the base abstractions that these packages extend.

To ensure that all integrations and their types interact with each other properly, it is important that they all use the same version of `@langchain/core`. When installing LangGraph, you should install `@langchain/core` alongside it as well:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-0-1)$npminstall@langchain/langgraph@langchain/core

```


`@langchain/core` must be installed separately because it is a peer dependency of `@langchain/langgraph`. This is to help package managers resolve a single version of `@langchain/core`.

Despite this, in some situations, your package manager may resolve multiple versions of core, which can result in unexpected TypeScript errors or other strange behavior. If you need to guarantee that you only have one version of `@langchain/core` is to add a `"resolutions"` or `"overrides"` field in your project's `package.json`. The specific field name will depend on your package manager. Here are a few examples:

Tip

The `resolutions` or `pnpm.overrides` fields for `yarn` or `pnpm` must be set in the root `package.json` file. Also note that we specify EXACT versions for resolutions. 

If you are using `yarn`, you should set `"resolutions"`[](https://yarnpkg.com/cli/set/resolution):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-2)"name":"your-project",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-3)"version":"0.0.0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-4)"private":true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-5)"engines":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-6)"node":">=18"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-7)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-8)"dependencies":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-9)"@langchain/anthropic":"^0.2.15",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-10)"@langchain/langgraph":"^0.2.0"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-11)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-12)"resolutions":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-13)"@langchain/core":"0.2.31"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-1-15)}

```


For `npm`, use `"overrides"`[](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#overrides):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-2)"name":"your-project",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-3)"version":"0.0.0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-4)"private":true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-5)"engines":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-6)"node":">=18"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-7)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-8)"dependencies":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-9)"@langchain/anthropic":"^0.2.15",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-10)"@langchain/langgraph":"^0.2.0"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-11)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-12)"overrides":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-13)"@langchain/core":"0.2.31"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-2-15)}

```


For `pnpm`, use the nested `"pnpm.overrides"`[](https://pnpm.io/package_json#pnpmoverrides) field:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-2)"name":"your-project",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-3)"version":"0.0.0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-4)"private":true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-5)"engines":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-6)"node":">=18"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-7)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-8)"dependencies":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-9)"@langchain/anthropic":"^0.2.15",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-10)"@langchain/langgraph":"^0.2.0"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-11)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-12)"pnpm":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-13)"overrides":{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-14)"@langchain/core":"0.2.31"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__codelineno-3-17)}

```


## Next steps[¶](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#next-steps "Permanent link")

You've now learned about some special considerations around using LangGraph.js with other LangChain ecosystem packages.

Next, check out [some how-to guides on core functionality](https://langchain-ai.github.io/langgraphjs/how-tos/#core).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/) [ Next  How to use LangGraph.js in web environments  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
