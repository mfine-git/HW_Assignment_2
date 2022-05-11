# Kovrr DevOps HW

## Introduction
Hi!
Firstly, thank you for taking the time to complete this assignment!

This document describes high level tasks, similar to what you may be asked to do at kovrr. 
The goal is to illustrate the expected technical demands from a junior DevOps engineer.

The task may require you to do some reading and learning. Nevertheless, if there is a question or you need more clarity, don't hesitate to contact us.

## Deliverables

- Please perform your work on this repository. `(Done)`
- Please include detailed instructions pertaining to how we should run your solution (can be in the readme or a separate txt file). `(Done)`
- Documentation as described in the guidelines below.
- Please notify us (Khen, Arnon or Lotem) when you are finished.

## Prerequisites

- Minikube (windows 10) [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)
- Docker (windows 10)
- Python (3.8 or above)
- Helm (tested on v3.9.0-rc.1 for Windows amd64) [https://github.com/helm/helm/releases](https://github.com/helm/helm/releases)
  * From Windows Command Promt (cmd) run: `setx PATH "path\to\helm.exe;%PATH%"`, restart cmd and check if helm is accessible from project folder: `helm version`

## Tasks

1. In this project in the `/app` directory there is a flask application which is executed as follows `python server.py <LISTEN_PORT>` 
Please add a Docker file to the container which runs the application to listen on port 3000. `(Done)`
```
IMPLEMENTATION
(See "/app/dockerfile") 
# From Pycharm IDE local terminal run:
> cd .\app\
> docker build --tag flask-image:v1 .
> docker run -d -p 3000:3000 --name flask-container flask-image:v1
# Open "http://localhost:3000/" in your browser to see "Hello from Flask !" message
# Uninstall: 
> docker stop flask-container
> docker rm flask-container
> docker rmi -f flask-image:v1
```

2. Create a github actions CI file that on every push to the `main` branch builds the above image on every commit. `(Done)`
```
IMPLEMENTATION
(See "/.github/workflows/actions-ci.yaml") 
# Push to `main` branch 
# Find "CI" Workflow runs at https://github.com/rotem08/devops_maxim/actions
```

3. Create a kubernetes deployment manifest with 3 replicas of the project container. `(Done)`
```
IMPLEMENTATION
(See "/deployment-manifest.yaml") 
# Open Windows PowerShell terminal as administrator and run:
> minikube status
> minikube start 
> minikube docker-env | Invoke-Expression
> cd .\app\
> docker build --tag flask-image:v1 .
> minikube dashboard --url (optionally)
# Open additional Windows PowerShell terminal as administrator and run:
> minikube tunnel
# Open "Kubernetes-dashboard" in your browser using url from command output (optionally)
# Return to Pycharm IDE local terminal and run:
> cd ..
> kubectl apply -f deployment-manifest.yaml
# See deployed resources via "Kubernetes-dashboard" or run:
> kubectl get deployments flask -o wide
> kubectl get rs -o wide (optionally)
> kubectl get pods -o wide (optionally)
```

4. Create kubernetes service manifest that exposes the app on port 8080. `(Done)`
```
IMPLEMENTATION
(See "/service-manifest.yaml")
# From Pycharm IDE local terminal run:
> kubectl apply -f service-manifest.yaml
> kubectl get svc flask (optionally)
# From Pycharm IDE local terminal run:
> kubectl get svc flask -o wide (optionally)
# Open "http://localhost:8080/" in your browser to see "Hello from Flask !" message
# Uninstall: 
# From Pycharm IDE local terminal run:
kubectl delete deployment flask; kubectl delete svc flask
```

<ins>Materials that were used during the execution of tasks 1-4:</ins>
- [https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)
- [https://docs.docker.com/ci-cd/github-actions/](https://docs.docker.com/ci-cd/github-actions/)
- [https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube](https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube)
- [https://kubernetes.io/docs/concepts/workloads/controllers/deployment/](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/)
- [https://minikube.sigs.k8s.io/docs/handbook/accessing/](https://minikube.sigs.k8s.io/docs/handbook/accessing/)

## Bonus

If possible, try to implement the features below 

5. Create a helm chart for the project. `(Done)`
```
IMPLEMENTATION
(See "/flask-chart" Helm directory)
# From Windows Command Promt (cmd) run:
> helm install flask-chart flask-chart/ --values flask-chart/values.yaml 
# Open "http://localhost:8080/" in your browser to see "Hello from Flask !" message
# Open "Kubernetes-dashboard" in your browser to observe deployed resources (optionally)
# From Pycharm IDE local terminal run:
> kubectl get all -o wide (optionally)
# Uninstall: 
# From Windows Command Promt (cmd) run:
> helm uninstall flask-chart
```
6. Add an API endpoint to the application for k8s liveness and readiness. `(Done)`  
```
IMPLEMENTATION
(See "/deployment-manifest.yaml") 
# Liveness and Readiness probes already exist in deployment-manifest.yaml (including Helm "flask-chart") 
# See probe's logs in "Kubernetes-dashboard" (open one of Flask pods) or:
# From Pycharm IDE local terminal run:
> kubectl logs $(kubectl get pod -l app=flask -o jsonpath="{.items[0].metadata.name}")
```

7. Expose prometheus metrics from the application `(not Done)`  
8. Create tests for the application `(not Done)`

<ins>Materials that were used during the execution of bonus part 5-8:</ins>
- [https://automateinfra.com/2021/04/19/how-to-create-your-first-helm-charts-kubernetes/](https://automateinfra.com/2021/04/19/how-to-create-your-first-helm-charts-kubernetes/)
- [https://faun.pub/health-check-live-and-readiness-probe-in-kubernetes-dd2ec0696e25](https://faun.pub/health-check-live-and-readiness-probe-in-kubernetes-dd2ec0696e25)

## Additional guidelines

- Please follow the used technology's best practices and guidelines `(Done)`
- Please document challenges and materials that were used during the execution of this task `(Done)`
- Keep the commit log clean and readable and make sure each feature (task step) is committed separately (you can use branching, squashing rebasing or any other git trick) `(Done)`
- Contact ronm@kovrr.com with any questions.

#### IMPORTANT NOTES:
- steps chronological order is critical (skipping steps may cause unexpected behavior) 
- each change related to rebuilding flask-image:v1 requires following steps (rm old image and start from task 3):
```# Open Windows PowerShell terminal as administrator and run:
> docker rmi -f flask-image:v1
> minikube status
> minikube stop 
> minikube start 
> minikube docker-env | Invoke-Expression
> cd .\app\
> docker build --tag flask-image:v1 .
```