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
  * [Docker Swarm](#docker_swarm)
  * [The 4 Services](#the-4-services)
  * [CI Pipeline](#ci-pipeline)
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

#### DnD Character Generator
* Service 1 (front-end): displays the results of the following 3 services for the user to see, as well as the last 5 characters created
* Service 2: returns a random name, race and class for the character
* Service 3: returns a random set of stats for the character by rolling 4 dice and removing the lowest of the 4
* Service 4: returns the stats plus stat bonuses based on the race of the character

## Architecture
### Risk Assessment
My initial risk assessment can be seen first, below is a refactored version from the end of the project outlinging the risks that I believe will pose problems to the service running smoothly
<br/>
![First Risk Assessment](https://i.imgur.com/PrJYhkk.png)
<br/><br/>
![Final Risk Assessment](https://i.imgur.com/IZoxt62.png)

View the original document [here](https://qalearning-my.sharepoint.com/:x:/g/personal/wdennington_qa_com/EdCGJbh2sVBIvNYGb5G1KQABv-aue0BOECjnMfE48c8-vw?e=XBopI8)

### Kanban Board
My initial trello board can be seen below. [Trello](https://trello.com) was used as it is free to use and allows easy movement of tasks along the timeline.

![Initial Trello Board](https://i.imgur.com/zwuWaGX.png)

My Final Trello Board can be seen below. It adds backend jobs as well as classification on whether or not a task was for the frontend or backend. This helped streamline work as tasks are now split into groups.

![Final Trello Board](https://i.imgur.com/sk4AEfM.png)

View the original board [here](https://trello.com/b/AJmOhN4i/dnd-char-generator)

### Analysis of Testing
Testing is an essential part of any successful project. Since this project is using a CI/CD approach, it is essential to automate testing to stop non functional versions making it to the live environment.

I have implemented unit tests, Jenkins runs them automatically and runs them before any other step to halt the build if the app is non functional.

![Jenkins build image](https://i.imgur.com/sAz6jQB.png)

## Infrastructure
Continuous deployment is implemented throughout my project in order to allow rapid and smooth development-to-deployment. The approach I have taken allows deploying a new version of the application with limited down-time.

### Jenkins
Whenever new content is pushed to the `development` branch, Github will send a webhook to Jenkins which Jenkins will use to initialise the build sequence detailed in its jenkinsfile build script.

#### **1.** Test: pytest  
> Unit tests are run as outlined earlier. A coverage report is produced and can be viewed in the console logs. 

#### **2.** & **3.** & **4.** Install, Build & Push: docker-compose  
> Docker is installed if the system does not have Docker install, this step is useful if the repository is cloned to a new machine to automate setup.
> The Docker images are built using their respective dockerfiles.
> Jenkins' credentials system is used to handle logging into DockerHub. The new images are then automatically pushed to Dockerhub.

#### **5.** Configure: ansible 
> Ansible configures several things:
> * Installing dependencies onto the swarm machines(such as docker and docker-compose),
> * Setting up the swarm, and joining the swarm on all worker nodes,
> * Reloading NGINX with any changes to the nginx.conf file.

#### **6.** Deploy: docker swarm/stack 
> Jenkins copies the `docker-compose.yaml` file over to the manager node, SSH's onto it, and then runs `docker stack deploy --compose-file`.

*The commands used in Jenkins' pipeline can be seen in the [Jenkinsfile](jenkins/Jenkinsfile)*

### CI Pipeline

Below is a visual representation of the full pipeline in visual form, from getting a task to deploying it to the live enviroment.

![CI Pipeline image](https://i.imgur.com/pUVClbM.jpg)

### Entity Diagram
This project only makes use of a single table. It is still important to describe the structure as describing elements of the table means each can be tested accordingly.

![entitity diagram image](https://i.imgur.com/XNea2JU.jpg)
 
### Docker Swarm

Using an orchestration tool, Docker Swarm, we are able to create a network of virtual machines that are all able to be accessed by the user to provide the same service. As shown in the pipeline diagram above I have implemented a load balancer using nginx, this upstreams the user to the least utilisied vm in the swarm. This also add extra security as the app is not accessed directly.

### The 4 Services
The diagram below represents how the services interact with one another. 

![diagram of the services](https://i.imgur.com/y8ulXOq.jpg)

The front end uses GET requests to get information from service 2 & 3 and send it to the frontend. This information is then sent to service 3 as a POST request, which sends back information based on the information obtained from service 2 & 3 by the frontend. The frontend can then display this to the user and store it in the database so the user can see some of the past characters generated.

## Development
### Front-End
When navigating to port 80 (default http port) on the NGINX's IP, the result is shown below. The nginx load balancer divides the traffic across the swarm to stop a single node from becoming overloaded. This result is displayed using HTML (with Jinja2) for the layout.

![image of front-end](https://i.imgur.com/KhgGRj2.png)

### Unit Testing
Unit testing is used here by seperating the services and testing each service with various scenarios. These are designed to assert each function returns an expected response under each given scenario. These tests are run automatically after every Git push using Jenkins. Jenkins prints out whether or not the tests were successsful, creates a cobertura report accessible on jenkins and also gives a coverage report noting the percentage of the application that was tested.

Below First is the cobertura report, next is the Junit Graph and finally is the coverage report.

![image of cobertura report](https://i.imgur.com/683BuWB.png)

Each service is tested individually so if any service does not function the test will fail and the build will stop.

![image of coverage report](https://i.imgur.com/3y9XgU5.png)

This coverage report indicates that every line in each of my routes has been tested at least once in some scenario in the unit testing. 

The precise lines used in my Jenkinsfile for testing are:
```py
python3 -m pytest 5000_templates --cov=5000_templates --cov-report=html --junitxml=junit/test-results1.xml --cov-report=xml --cov-report term-missing
python3 -m pytest 5001_name_class --cov=5001_name_class --cov-report=html --junitxml=junit/test-results2.xml --cov-report=xml --cov-report term-missing
python3 -m pytest 5002_stats --cov=5002_stats --cov-report=html --junitxml=junit/test-results3.xml --cov-report=xml --cov-report term-missing
python3 -m pytest 5003_character --cov=5003_character --cov-report=html --junitxml=junit/test-results4.xml --cov-report=xml --cov-report term-missing
 ```
 This runs the tests on each service respectively. 
 
This result also produces a junit.xml file which is used by the Jenkins Junit plug-in to produce advanced testing reports, further easing traceback for the developer. An example of these results can be seen below.

![image of Junit](https://i.imgur.com/15lzXxI.png)
![image of advanced coverage report](https://i.imgur.com/FqiOZ03.png)


## Footer
### Future Improvements
* Reduce down-time on the deploy stage 
* Allow users to add their own homebrew races along with their stat modifiers.
* Improve testing to include integration testing.

### Author
William Dennington

### Acknowledgements
* [Harry Volker](https://github.com/htr-volker)
* [Oliver Nichols](https://github.com/OliverNichols) 


