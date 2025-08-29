**Contents** </br>
- [Introduction](#introduction)
- [Practicals](#practicals)
  - [Install GitHub CLI](#install-github-cli)
  - [VS Code GitHub Actions](#vs-code-github-actions)
- [Components of GitHub Actions](#components-of-github-actions)
- [References](#references)

# Introduction
GitHub Actions is an end-to-end workflow automation platform that handles continuous integration and continuous delivery (CI/CD) aspect for Git and GitHub. As a CI/CD automation tools, GitHub Actions helps deliver software as soon as possible to its users. While GitHub allows collaboration on writing software code, GitHub Actions enables fast delivery of the software to users. 

Before GitHub Actions was available, other tooling (e.g., Jenkins, Travis CI) needed to be integrated on GitHub to facilitate CI/CD. While GitHub Actions is one of the popular tools, there are other alternatives such [Azure DevOps](https://azure.microsoft.com/en-us/products/devops), [Jenkins](https://www.jenkins.io/), [Travis CI](https://www.travis-ci.com/), and [CircleCI](https://circleci.com/). The advantage of GitHub Actions is that its is natively integrated to other GitHub components.

GitHub Actions are triggered by events in GitHub such as **pull** and **push** requests, leading to automated CI/CD workflows. GitHub Actions defines what should happen following *push* and *pull* requests (e.g., build code on *push*, and *release code* if build is successful). CI/CD code files for GitHub Actions can be stored on GitHub alongside the software source code. In other words, GitHub will contain both source codes for the application software as well as the CI/CD automation.

A typical flow in Event (e.g., push, pull) occurs --- Trigger **workflow** definition --> starts **jobs** on designated systems (**runners**). **Jobs**: steps for a predefined **action** or run a Shell command.
- **Actions Marketplace**: repository to publish and share *actions*.
- 

For self-hosted runners (systems) and for public repositories, GitHub Actions is free.
# Practicals
## Install GitHub CLI
This avoids managing tokens manually.
```bash
    sudo apt install gh # Install GitHub CLI if you don’t have it
    gh auth login # # Log in interactively (opens browser)
    # Note: GitHub.com -- HTTPS -- Authenticate with GitHub credentials -- Login with a web browser --> Copy one-time code to authenticate on GitHub.com.
```
<p align="left">
<img src="figures/github_cli.png" style="max-width:50%; height:auto;">
</p>
<p align="left"><strong>Figure 1:</strong> Logging using GitHub CLI ($gh auth login) </p>

Create workflows under **.github/workflows**
```bash
cd gitops
mkdir .github
cd .github
mkdir workflows
cd .github/workflows
nano build-sample.yml
cd ../../
git add .github/
git commit -m "Create workflows."
git push origin main
```

The above "*git push origin main*" is one event that can trigger execution of the workflow. Figure 2 shows execution of the workflow on GitHub Actions following the "*push*" event.
<figure>
  <table>
    <tr>
      <td>
        <img src="figures/workflow_1.png" style="max-width:100%; height:auto;">
      </td>
      <td>
        <img src="figures/eks_aws_console_4.png" style="max-width:100%; height:auto;">
      </td>
    </tr>
  </table>
  <figcaption><strong>Figure 2: </strong> Push event vs Workflow on GitHub Actions </figcaption>
  </figure>


## VS Code GitHub Actions

# Components of GitHub Actions
- Events that trigger automation: occurs due to a change on a GitHub repository, which is identified by a Secure Hashing Algorithm SHA1 value. 
- Parts that achieve the automation: 
  - **workflows** directory that contains action files to be executed in response to events.
  - Workflows are files in YAML format inside **.github/workflows** directory within the GitHub repository.
  - In each workflow, there are **jobs** that can run in parallel when the workflow is triggered.
  - Each job consists of **steps**, which execute shell commands or GitHub actions.
  - **Runner**: a server that executes steps in a job.



# References
* Learning GitHub Actions by Brent Laster (O’Reilly). Copyright 2023 Tech Skills Transformations, LLC, 978-1-098-13107-4.
* https://github.com/techupskills/learning-github-actions
* 