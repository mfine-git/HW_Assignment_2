# Kovrr DevOps HW

## Introduction
Hi!
Firstly, thank you for taking the time to complete this assignment!

This document describes high level tasks, similar to what you may be asked to do at kovrr. 
The goal is to illustrate the expected technical demands from a junior DevOps engineer.

The task may require you to do some reading and learning. Nevertheless, if there is a question or you need more clarity, don't hesitate to contact us.

## Deliverables

- Please perform your work on this repository.
- Please include detailed instructions pertaining to how we should run your solution (can be in the readme or a separate txt file).
- Documentation as described in the guidelines below.
- Please notify us (Khen, Arnon or Lotem) when you are finished.

## Prerequisites

- minikube [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)
- docker
- python (3.8 or above)

## Tasks

1. In this project in the `app` directory there is a flask application which is executed as follows `python server.py <LISTEN_PORT>` 
Please add a Docker file to the container which runs the application to listen on port 3000
2. Create a github actions CI file that on every push to the `master` branch builds the above image on every commit
3. Create a kubernetes deployment manifest with 3 replicas of the project container
4. Create a kubernetes manifest that exposes this service on port 8080

## Bonus

If possible, try to implement the features below 

- Create a helm chart for the project
- Add an API endpoint to the application for k8s liveness and readiness 
- Expose prometheus metrics from the application
- Create tests for the application

## Additional guidelines

- Please follow the used technology's best practices and guidelines
- Please document challenges and materials that were used during the execution of this task
- Keep the commit log clean and readable and make sure each feature (task step) is committed separately (you can use branching, squashing rebasing or any other git trick)
- Contact ronm@kovrr.com with any questions.
