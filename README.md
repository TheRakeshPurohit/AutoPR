<div align="center">

<img src="website/static/img/AutoPR_Mark_color.png" alt="AutoPR logo" width=300 />

<h1>🌳 AutoPR 🌳</h1>

[![Discord](https://badgen.net/badge/icon/discord?icon=nope&label&color=purple)](https://discord.gg/ykk7Znt3K6)
[![Docs](https://badgen.net/badge/icon/docs?icon=docs&label&color=blue)](https://docs.autopr.com)

Breathe life into your codebase

</div>

## 🌟 Features

🌳 Living summaries of your code in nested READMEs
📄 Summarize changes by adding a "summarize" label to a PR  


... more coming soon!

## 🚀 Getting Started

Please see the [installation guide](https://docs.autopr.com/installing/github).

---

Below is an example of AutoPR's Living README:

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files and folders related to a Python project. The `Dockerfile` sets up a Docker image for the project, while the `LICENSE.md` file contains the MIT License for the software. The `Makefile` is used for automating development tasks, and the `action.yml` file configures an automatic pull request workflow. The `autopr` folder contains code and configuration files for an autonomous agent system, including actions, services, and workflows. The `entrypoint.sh` script sets the Git configuration and runs the application. The `poetry.lock` and `pyproject.toml` files are used by the Poetry package manager. There are also JSON schema files for defining strict workflows and trigger configurations.


### [`Dockerfile`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./Dockerfile)

🏗️ Sets up a Docker image based on the `duffn/python-poetry:3.9-bullseye` image    
🔧 Installs git from the bullseye-backports repository    
📥 Copies an entrypoint script and makes it executable    
📥 Copies the `pyproject.toml` and `poetry.lock` files    
🔧 Activates the virtual environment and installs the project dependencies using Poetry    
📥 Copies the rest of the files to the `/app` directory    
🔧 Installs the application using Poetry    
🚀 Sets the entrypoint to `/entrypoint.sh` for running the app    


### [`LICENSE.md`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./LICENSE.md)

📄 This file contains the MIT License.  
🔒 The license grants permission to use, modify, and distribute the software.  
📝 The license requires the copyright notice and permission notice to be included in all copies.  
🚫 The software is provided "as is" without warranty.  
📅 The license is valid until 2023.  
💼 The license is owned by Raphael Francis Ltd.  


### [`Makefile`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./Makefile)

📝 This file is a makefile-like configuration file.  
🔧 It defines various targets and their associated commands.  
💻 The targets are: `format`, `type`, `test`, `schema`, and `all`.  
🔧 The `format` target runs a command to format code using the `black` tool.  
🔧 The `type` target runs a command to perform type checking using `pyright`.  
🔧 The `test` target runs pytest on the `autopr/tests` directory.  
🔧 The `schema` target runs a command to generate configuration entrypoints using `autopr.models.config`.  
🔧 The `all` target runs all the targets in sequence: `format`, `type`, `test`, and `schema`.  
🔧 This file is meant to automate common development tasks and ensure code quality.  


### [`action.yml`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./action.yml)

📄 This file is a configuration file for an automatic pull request workflow.  
🔧 It specifies the details for running the workflow, such as the Docker image to use.  
🎨 It also includes branding information, such as the icon and color to use.  
🔑 The file defines inputs required for the workflow, such as the GitHub token and base branch.  
🎥 It includes a default loading GIF URL to display while the pull request is being generated.  
🌿 The file defines a template for the name of the target branch.  
🔄 It specifies whether to overwrite existing branches and pull requests when creating from issues.  


### [`autopr/`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./autopr)

This folder contains a collection of Python files and folders that make up an autonomous agent system. The "actions" folder contains reusable actions for automated processes or scripts, while the "gh_actions_entrypoint.py" file orchestrates the execution of a GitHub Actions workflow. The "log_config.py" file configures logging settings, and the "main.py" file serves as the main entry point for the application. The "models" folder provides code and configuration files for building and executing workflows, and the "services" folder contains classes and services for managing and running actions. The "triggers.py" file retrieves trigger configurations, and the "workflows" folder contains YAML files that define various automation processes.  


### [`entrypoint.sh`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./entrypoint.sh)

📝 The file is a shell script  
🔧 It sets the Git configuration for a specific directory  
✉️ It sets the user email and name for Git commits  
📦 It activates a virtual environment  
🐍 It runs a Python module called `autopr.gh_actions_entrypoint`  


### [`poetry.lock`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./poetry.lock)

📄 This file is an executive summary  of a project or report  
🔍 It provides a high-level overview of the main points  
📝 It highlights key findings, conclusions, and recommendations  
📊 It may include a summary of data or analysis  
👥 It is intended for someone who is new to the project or report  
🚫 It does not include trivial details or technical explanations  
💡 It gives a clear understanding of the purpose and scope of the project  
👀 It provides a quick glance at the content without going into depth  
💼 It serves as a starting point for further exploration or discussion  
📌 It is concise and easy to read, even if the file is empty  


### [`pyproject.toml`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./pyproject.toml)

📋 This file is a configuration file for a Python project using Poetry.  
🔍 It contains information about the project's name, version, and authors.  
📄 The license of the project is specified as MIT.  
📦 It lists the packages and their dependencies required for the project.  
🧪 There are separate dependencies for testing and development.  
🔧 The build system used is Poetry.  
🔍 The file also includes configuration for the Pyright static type checker.  
🔍 It specifies the line length and target version for the Black code formatter.  


### [`strict_workflow_schema.json`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./strict_workflow_schema.json)

📄 The file is a JSON schema describing a strict workflow definition.  
🔍 It defines various actions that can be performed within the workflow.  
🔀 Actions include commenting, setting issue titles, walking files, making API calls, running bash commands, and more.  
📝 Each action has its own set of inputs and outputs.  
🔄 The workflow steps are defined as an array of actions.  
📚 The schema also includes definitions for various data types and declarations used within the actions.  
📝 The purpose of the file is to provide a standardized structure for defining and executing strict workflows.  
🗂️ The schema can be used to validate and ensure the correctness of workflow definitions.  
🧩 It allows for easy integration with other tools and systems that support the schema.  
📚 The file can serve as a reference for understanding the structure and capabilities of strict workflows.  


### [`trigger_schema.json`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./trigger_schema.json)

📋 This file is a JSON schema that defines the structure and properties of various action models and trigger configurations.  
📝 It contains definitions for different types of actions, such as commenting, making API calls, walking files, and more.  
🔄 The file also includes definitions for iterable versions of these actions, which can be used in loop-like workflows.  
🕒 It defines a CronTrigger configuration for scheduling actions based on cron expressions.  
🔀 The TopLevelTriggerConfig object is the main configuration that can contain multiple triggers.  
🔗 The triggers can be label triggers, comment triggers, push triggers, or cron triggers.  
⚙️ Each trigger has its own set of properties and can be used to define custom workflows and automation tasks.  
💡 The file provides a comprehensive schema for building and configuring workflows in a structured and standardized manner.  
🛠️ It can be used as a reference to validate and generate workflows, ensuring consistency and correctness.  
📚 The file is designed to be easily extensible, allowing for the addition of new action models and trigger configurations.  


### [`workflow_schema.json`](https://github.com/raphael-francis/AutoPR-internal/blob/58930ae93625b5c6df53ea36ba4305031b0615d6/./workflow_schema.json)

📄 This file is a JSON schema definition for a workflow definition.  
🔧 It defines various types and properties for different actions and declarations used in the workflow.  
📝 The schema includes definitions for actions like commenting, setting issue title, walking files, making API calls, running bash commands, etc.  
📚 It also defines different types of declarations like template, variable, constant, and lambda declarations.  
📋 The workflow definition includes a name, description, inputs, and outputs.  
🔢 It consists of a list of steps which can be actions, workflow invocations, or conditional statements.  
🔀 Conditional statements can have if-else branches and support different conditions like lambda expressions and context checks.  
🔄 Workflow invocations can be either regular or iterable.  
🔑 Overall, this file provides a structured definition for creating and executing workflows with various actions and conditions.  

<!-- Living README Summary -->