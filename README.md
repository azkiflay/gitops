**Contents** </br>
- [Introduction](#introduction)
- [References](#references)

# Introduction
GitHub Actions is an end-to-end workflow automation platform that handles continuous integration and continuous delivery (CI/CD) aspect for Git and GitHub. As a CI/CD automation tools, GitHub Actions helps deliver software as soon as possible to its users. While GitHub allows collaboration on writing software code, GitHub Actions enables fast delivery of the software to users. 

Before GitHub Actions was available, other tooling (e.g., Jenkins, Travis CI) needed to be integrated on GitHub to facilitate CI/CD. While GitHub Actions is one of the popular tools, there are other alternatives such [Azure DevOps](https://azure.microsoft.com/en-us/products/devops), [Jenkins](https://www.jenkins.io/), [Travis CI](https://www.travis-ci.com/), and [CircleCI](https://circleci.com/). The advantage of GitHub Actions is that its is natively integrated to other GitHub components.

GitHub Actions are triggered by events in GitHub such as **pull** and **push** requests, leading to automated CI/CD workflows. GitHub Actions defines what should happen following *push* and *pull* requests (e.g., build code on *push*, and *release code* if build is successful). CI/CD code files for GitHub Actions can be stored on GitHub alongside the software source code. In other words, GitHub will contain both source codes for the application software as well as the CI/CD automation.

- Event (e.g., push, pull) occurs --- Trigger **workflow** definition --> starts **jobs** on designated systems (**runners**). **Jobs**: steps for a predefined **action** or run a Shell command.
- **Actions Marketplace**: repository to publish and share *actions*.


# References
* Learning GitHub Actions by Brent Laster (O’Reilly). Copyright 2023 Tech Skills Transformations, LLC, 978-1-098-13107-4.
* https://github.com/techupskills/learning-github-actions
* 