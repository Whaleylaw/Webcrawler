---
url: https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#how-to-deploy-to-langgraph-cloud)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to Deploy to LangGraph Cloud 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/?q= "Share")

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
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
          * [ Application Structure  ](https://langchain-ai.github.io/langgraphjs/how-tos#application-structure)
          * Deployment  Deployment 
            * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/how-tos#deployment)
            * How to Deploy to LangGraph Cloud  [ How to Deploy to LangGraph Cloud  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/) Table of contents 
              * [ Prerequisites  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#prerequisites)
              * [ Create New Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#create-new-deployment)
              * [ Create New Revision  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#create-new-revision)
              * [ View Build and Server Logs  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#view-build-and-server-logs)
              * [ Interrupt Revision  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#interrupt-revision)
              * [ Delete Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#delete-deployment)
              * [ Deployment Settings  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#deployment-settings)
            * [ How to do a Self-hosted deployment of LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/deploy-self-hosted/)
            * [ How to interact with the deployment using RemoteGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraphjs/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraphjs/how-tos#assistants)
          * [ Threads  ](https://langchain-ai.github.io/langgraphjs/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming_1)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop_1)
          * [ Double-texting  ](https://langchain-ai.github.io/langgraphjs/how-tos#double-texting)
          * [ Webhooks  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/webhooks/)
          * [ Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs/)
          * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-studio)
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

  * [ Prerequisites  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#prerequisites)
  * [ Create New Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#create-new-deployment)
  * [ Create New Revision  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#create-new-revision)
  * [ View Build and Server Logs  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#view-build-and-server-logs)
  * [ Interrupt Revision  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#interrupt-revision)
  * [ Delete Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#delete-deployment)
  * [ Deployment Settings  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#deployment-settings)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Deployment  ](https://langchain-ai.github.io/langgraphjs/how-tos#deployment)



# How to Deploy to LangGraph Cloud[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#how-to-deploy-to-langgraph-cloud "Permanent link")

LangGraph Cloud is available within [LangSmith](https://www.langchain.com/langsmith). To deploy a LangGraph Cloud API, navigate to the [LangSmith UI](https://smith.langchain.com/).

## Prerequisites[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#prerequisites "Permanent link")

  1. LangGraph Cloud applications are deployed from GitHub repositories. Configure and upload a LangGraph Cloud application to a GitHub repository in order to deploy it to LangGraph Cloud.
  2. [Verify that the LangGraph API runs locally](https://langchain-ai.github.io/langgraphjs/cloud/deployment/test_locally/). If the API does not run successfully (i.e. `langgraph dev`), deploying to LangGraph Cloud will fail as well.



## Create New Deployment[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#create-new-deployment "Permanent link")

Starting from the [LangSmith UI](https://smith.langchain.com/)...

  1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
  2. In the top-right corner, select `+ New Deployment` to create a new deployment.
  3. In the `Create New Deployment` panel, fill out the required fields.
    1. `Deployment details`
      1. Select `Import from GitHub` and follow the GitHub OAuth workflow to install and authorize LangChain's `hosted-langserve` GitHub app to access the selected repositories. After installation is complete, return to the `Create New Deployment` panel and select the GitHub repository to deploy from the dropdown menu. **Note** : The GitHub user installing LangChain's `hosted-langserve` GitHub app must be an [owner](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-owners) of the organization or account.
      2. Specify a name for the deployment.
      3. Specify the desired `Git Branch`. A deployment is linked to a branch. When a new revision is created, code for the linked branch will be deployed. The branch can be updated later in the [Deployment Settings](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#deployment-settings).
      4. Specify the full path to the [LangGraph API config file](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#configuration-file) including the file name. For example, if the file `langgraph.json` is in the root of the repository, simply specify `langgraph.json`.
      5. Check/uncheck checkbox to `Automatically update deployment on push to branch`. If checked, the deployment will automatically be updated when changes are pushed to the specified `Git Branch`. This setting can be enabled/disabled later in the [Deployment Settings](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#deployment-settings).
    2. Select the desired `Deployment Type`.
      1. `Development` deployments are meant for non-production use cases and are provisioned with minimal resources.
      2. `Production` deployments can serve up to 500 requests/second and are provisioned with highly available storage with automatic backups.
    3. Determine if the deployment should be `Shareable through LangGraph Studio`.
      1. If unchecked, the deployment will only be accessible with a valid LangSmith API key for the workspace.
      2. If checked, the deployment will be accessible through LangGraph Studio to any LangSmith user. A direct URL to LangGraph Studio for the deployment will be provided to share with other LangSmith users.
    4. Specify `Environment Variables` and secrets. See the [Environment Variables reference](https://langchain-ai.github.io/langgraphjs/cloud/reference/env_var/) to configure additional variables for the deployment.
      1. Sensitive values such as API keys (e.g. `OPENAI_API_KEY`) should be specified as secrets.
      2. Additional non-secret environment variables can be specified as well.
    5. A new LangSmith `Tracing Project` is automatically created with the same name as the deployment.
  4. In the top-right corner, select `Submit`. After a few seconds, the `Deployment` view appears and the new deployment will be queued for provisioning.



## Create New Revision[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#create-new-revision "Permanent link")

When [creating a new deployment](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#create-new-deployment), a new revision is created by default. Subsequent revisions can be created to deploy new code changes.

Starting from the [LangSmith UI](https://smith.langchain.com/)...

  1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
  2. Select an existing deployment to create a new revision for.
  3. In the `Deployment` view, in the top-right corner, select `+ New Revision`.
  4. In the `New Revision` modal, fill out the required fields.
    1. Specify the full path to the [LangGraph API config file](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#configuration-file) including the file name. For example, if the file `langgraph.json` is in the root of the repository, simply specify `langgraph.json`.
    2. Determine if the deployment should be `Shareable through LangGraph Studio`.
      1. If unchecked, the deployment will only be accessible with a valid LangSmith API key for the workspace.
      2. If checked, the deployment will be accessible through LangGraph Studio to any LangSmith user. A direct URL to LangGraph Studio for the deployment will be provided to share with other LangSmith users.
    3. Specify `Environment Variables` and secrets. Existing secrets and environment variables are prepopulated. See the [Environment Variables reference](https://langchain-ai.github.io/langgraphjs/cloud/reference/env_var/) to configure additional variables for the revision.
      1. Add new secrets or environment variables.
      2. Remove existing secrets or environment variables.
      3. Update the value of existing secrets or environment variables.
  5. Select `Submit`. After a few seconds, the `New Revision` modal will close and the new revision will be queued for deployment.



## View Build and Server Logs[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#view-build-and-server-logs "Permanent link")

Build and server logs are available for each revision.

Starting from the `LangGraph Platform` view...

  1. Select the desired revision from the `Revisions` table. A panel slides open from the right-hand side and the `Build` tab is selected by default, which displays build logs for the revision.
  2. In the panel, select the `Server` tab to view server logs for the revision. Server logs are only available after a revision has been deployed.
  3. Within the `Server` tab, adjust the date/time range picker as needed. By default, the date/time range picker is set to the `Last 7 days`.



## Interrupt Revision[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#interrupt-revision "Permanent link")

Interrupting a revision will stop deployment of the revision.

Undefined Behavior

Interrupted revisions have undefined behavior. This is only useful if you need to deploy a new revision and you already have a revision "stuck" in progress. In the future, this feature may be removed.

Starting from the `LangGraph Platform` view...

  1. Select the menu icon (three dots) on the right-hand side of the row for the desired revision from the `Revisions` table.
  2. Select `Interrupt` from the menu.
  3. A modal will appear. Review the confirmation message. Select `Interrupt revision`.



## Delete Deployment[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#delete-deployment "Permanent link")

Starting from the [LangSmith UI](https://smith.langchain.com/)...

  1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
  2. Select the menu icon (three dots) on the right-hand side of the row for the desired deployment and select `Delete`.
  3. A `Confirmation` modal will appear. Select `Delete`.



## Deployment Settings[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#deployment-settings "Permanent link")

Starting from the `LangGraph Platform` view...

  1. In the top-right corner, select the gear icon (`Deployment Settings`).
  2. Update the `Git Branch` to the desired branch.
  3. Check/uncheck checkbox to `Automatically update deployment on push to branch`.
    1. Branch creation/deletion and tag creation/deletion events will not trigger an update. Only pushes to an existing branch will trigger an update.
    2. Pushes in quick succession to a branch will not trigger subsequent updates. In the future, this functionality may be changed/improved.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/graph_rebuild/) [ Next  How to do a Self-hosted deployment of LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/deploy-self-hosted/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
