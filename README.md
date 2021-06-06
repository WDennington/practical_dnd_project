# practical_dnd_project

## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Kanban Board](#kanban-board)
  * [Test Analysis](#analysis-of-testing)
* [Infrastructure](#infrastructure)
  * [Jenkins](#jenkins)
  * [Entity Diagram](#entity-diagram)
  * [Docker Swarm](#interactions-diagram)
  * [The 4 Services](#the-4-services)
* [Development](#development)
  * [Front-End Design](#front-end)
  * [Unit Testing](#unit-testing)
* [Footer](#footer)

## Introduction

### Objective
The objective provided for this project is as follows:
> To create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

These 4 services will be 1 frontend service, 2 backend services and a third backend service which takes information from service 2 and 3 to generate some information.

The following constraints were also set:
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
* Database Layer: MySQL

### Proposal
To make a DnD character/stats generator

#### Weapons Generator
* Service 1 (front-end): displays the results of the following 3 services for the user to see, as well as the last 5 characters created
* Service 2: returns a random name, race and class for the character
* Service 3: returns a random set of stats for the character by rolling 4 dice and removing the lowest of the 4
* Service 4: returns the stats plus stat bonuses based on the race of the character

## Architecture
### Risk Assessment
My initial risk assessment can be seen first, below is a refactored version from the end of the project outlinging the risks that I believe will pose problems to the service running smoothly
<br/>
![Imgur](https://i.imgur.com/PrJYhkk.png)
<br/><br/>
![Imgur](https://i.imgur.com/PmmhgTE.png)

View the original document [here](https://qalearning-my.sharepoint.com/:x:/g/personal/wdennington_qa_com/EdCGJbh2sVBIvNYGb5G1KQABv-aue0BOECjnMfE48c8-vw?e=XBopI8)

