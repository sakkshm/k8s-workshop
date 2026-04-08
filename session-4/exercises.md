# Section 4 Exercises

## Exercise 1: Inspect the Cluster

### Task
Check the status of your Kubernetes cluster.

```bash
kubectl get nodes
kubectl get pods -A
````

### Questions

* How many nodes are present?
* Which node is the control plane?
* What system Pods are running?

## Exercise 2: Understand Cluster State

### Task

Describe a node.

```bash
kubectl describe node <node-name>
```

### Questions

* What resources does the node have?
* What conditions are reported?
* What is the node status?

## Exercise 3: Deploy an Application

### Task

Create a deployment.

```bash
kubectl create deployment demo-nginx --image=nginx
```

### Questions

* What objects are created behind the scenes?
* What is the desired state defined here?
* How many Pods are running?

## Exercise 4: Inspect Deployment

### Task

Describe the deployment.

```bash
kubectl describe deployment demo-nginx
```

### Questions

* What is the replica count?
* What image is used?
* What events are shown?

## Exercise 5: List Pods

### Task

View Pods.

```bash
kubectl get pods
```

### Questions

* What is the Pod status?
* What happens during Pod startup?
* What does the READY column mean?

## Exercise 6: Expose Application

### Task

Expose the deployment.

```bash
kubectl expose deployment demo-nginx --type=NodePort --port=80
kubectl get svc
```

### Questions

* What is a Service?
* What is NodePort?
* How do you access the application?

## Exercise 7: Access the Application

### Task

Access the app via browser or curl.

```bash
curl http://<node-ip>:<nodeport>
```

### Questions

* How does traffic reach the Pod?
* What components are involved?
* What happens if a Pod is down?

## Exercise 8: Scaling

### Task

Scale the deployment.

```bash
kubectl scale deployment demo-nginx --replicas=3
kubectl get pods -o wide
```

### Questions

* Where are Pods scheduled?
* How does Kubernetes decide placement?
* Is scaling imperative or declarative?

## Exercise 9: Logs and Debugging

### Task

View logs.

```bash
kubectl logs <pod-name>
kubectl logs -f <pod-name>
```

### Questions

* What information do logs provide?
* Why is streaming logs useful?
* How does this compare to Docker logs?

## Exercise 10: Describe Pod

### Task

Inspect a Pod in detail.

```bash
kubectl describe pod <pod-name>
```

### Questions

* What events are shown?
* What errors can appear here?
* Why is this command important?

## Exercise 11: Self-Healing

### Task

Delete a Pod.

```bash
kubectl delete pod <pod-name>
kubectl get pods -w
```

### Questions

* Why does the Pod come back?
* Which component is responsible?
* What is the reconciliation loop?

## Exercise 12: Failure Debugging

### Task

Deploy a broken configuration.

```bash
kubectl apply -f broken.yaml
```

### Questions

* What is the Pod status?
* What error do you see in describe?
* How do you fix it?

## Exercise 13: Node Drain

### Task

Drain a node.

```bash
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
kubectl get pods -o wide
```

### Questions

* What happens to Pods on that node?
* Where are they moved?
* Why is this useful?

## Exercise 14: Node Failure Simulation

### Task

Simulate node failure (shutdown VM or disconnect network).

### Questions

* What happens to node status?
* What happens to Pods?
* How long does recovery take?

## Exercise 15: Scheduling Behavior

### Task

Observe Pod placement.

```bash
kubectl get pods -o wide
```

### Questions

* Are Pods evenly distributed?
* What factors affect scheduling?
* What happens if a node has no resources?

## Exercise 16: Observability Basics

### Task

Check resource usage (if metrics-server installed).

```bash
kubectl top nodes
kubectl top pods
```

### Questions

* Which node is most utilized?
* Which Pod consumes most resources?
* Why is observability important?

## Exercise 17: Service Behavior

### Scenario

Multiple Pods behind a Service.

### Questions

* How does load balancing work?
* What happens if one Pod crashes?
* Does the Service IP change?

## Exercise 18: Desired vs Actual State

### Scenario

Deployment specifies 3 replicas, but only 2 Pods are running.

### Questions

* What does Kubernetes do?
* Which components act?
* How is the state corrected?

## Exercise 19: End-to-End Flow

### Task

Trace a request:

Client → Node → Service → Pod

### Questions

* What path does the request follow?
* What role does kube-proxy play?
* Where does load balancing occur?

## Exercise 20: Thought Experiment

### Scenario

You need to run:

* 50 microservices
* Auto-scaling
* High availability

### Questions

* Why is Kubernetes necessary?
* What problems does it solve?
* What would be difficult without it?

## Final Check

You should now understand:

* Kubernetes architecture (control plane vs workers)
* Core objects (Pods, Deployments, Services)
* Scaling and scheduling
* Self-healing and failure recovery
* Debugging using logs and describe
* Declarative system behavior

