# Kubernetes in Action (Live Demo + System Behavior)

## Overview

This section builds on everything so far:

* Section 1 → Processes → Containers
* Section 2 → Docker (single machine)
* Section 3 → Distributed infrastructure

Now:

> Kubernetes manages containers **across multiple machines automatically**

This section focuses on:

* How Kubernetes works conceptually
* How it behaves in real scenarios
* How it handles failures and scaling

---

## Learning Objectives

By the end of this section, you should be able to:

* Explain why Kubernetes is needed
* Understand Kubernetes architecture
* Use `kubectl` to interact with a cluster
* Deploy, expose, and scale applications
* Debug issues using logs and describe
* Understand self-healing and scheduling behavior

---

## 1. Why Kubernetes?

### Problem Without Kubernetes

Managing containers across multiple machines manually:

```bash
ssh node1 "docker run app"
ssh node2 "docker run app"
ssh node3 "docker run app"
```

### Issues

* No centralized view
* No automatic recovery
* No scheduling logic
* No scaling automation

---

### Solution

> Kubernetes = Container Orchestration System

It automates:

* Scheduling containers
* Restarting failed workloads
* Scaling applications
* Managing networking

---

### Key Insight

> Kubernetes replaces manual operational work with automation

---

## 2. Kubernetes Architecture (Big Picture)

### Cluster Structure

```text
Control Plane
   ↓
Worker Nodes (run workloads)
```

---

### Responsibilities

| Component     | Role            |
| ------------- | --------------- |
| Control Plane | Decision making |
| Worker Nodes  | Execution       |

---

### Analogy

* Control Plane → Air traffic control
* Worker Nodes → Airplanes

---

## 3. Control Plane Components

### API Server

* Entry point for all operations
* Validates and processes requests

```bash
kubectl → API Server
```

---

### etcd

* Key-value store
* Stores **entire cluster state**

---

### Scheduler

* Assigns Pods to nodes
* Considers:

  * CPU
  * Memory
  * Constraints

---

### Controller Manager

* Ensures desired state = actual state
* Recreates failed Pods

---

### Key Insight

> Kubernetes is a **control loop system**, not a one-time execution engine

---

## 4. Core Kubernetes Objects

### Pod

* Smallest deployable unit
* Usually contains one container

---

### Deployment

* Manages Pods
* Ensures:

  * Replica count
  * Updates
  * Rollbacks

---

### Service

* Stable network endpoint
* Routes traffic to Pods

---

### Mental Model

```text
Deployment → Pods → Containers
        ↑
     Service (access layer)
```

---

### Key Insight

> You define **desired state**, Kubernetes enforces it

---

## 5. Our Setup (k3s Cluster)

### Infrastructure

* 1 Control Plane node
* 2 Worker nodes
* Running on Proxmox VMs

---

### Access

From control machine:

```bash
kubectl
```

---

### Why k3s?

* Lightweight Kubernetes
* Low resource usage
* Same API as full Kubernetes

---

## 6. Demo Step 1: Inspect the Cluster

### Commands

```bash
kubectl get nodes
kubectl get pods -A
```

---

### Expected Output

* 3 nodes (1 control, 2 workers)
* System Pods:

  * CoreDNS
  * metrics-server

---

### Interpretation

* `READY` → node healthy
* `ROLES` → control-plane / worker

---

### Debug Tip

If nodes are `NotReady`:

* Check network
* Check kubelet status

---

## 7. Demo Step 2: Deploy Application

### Command

```bash
kubectl create deployment demo-nginx --image=nginx
```

---

### Verify

```bash
kubectl get pods
```

---

### What Happens Internally

1. Deployment created
2. ReplicaSet created
3. Pod created
4. Scheduler assigns node
5. Pod runs container

---

### Inspect

```bash
kubectl describe deployment demo-nginx
```

---

### Key Insight

> One command triggers multiple internal components

---

## 8. Exposing the Application (NodePort)

### Command

```bash
kubectl expose deployment demo-nginx --type=NodePort --port=80
kubectl get svc
```

---

### Output

```text
PORT(S): 80:30080/TCP
```

---

### Access

```text
http://<node-ip>:30080
```

---

### How It Works

```text
Client → NodePort → Service → Pod
```

---

### Key Clarification

* NodePort opens port on **every node**
* Service distributes traffic across Pods

---

## 9. Scaling the Application

### Command

```bash
kubectl scale deployment demo-nginx --replicas=3
```

---

### Verify

```bash
kubectl get pods -o wide
```

---

### Observation

* Pods distributed across nodes

---

### Key Insight

> Scaling is declarative — not manual repetition

---

## 10. Observability (Conceptual)

### Tools

* Metrics Server → basic metrics
* Prometheus → metrics collection
* Grafana → dashboards

---

### Example

```bash
kubectl top nodes
kubectl top pods
```

---

### What You Learn

* CPU usage
* Memory usage
* Resource bottlenecks

---

### Key Insight

> You cannot operate distributed systems without observability

---

## 11. Debugging in Kubernetes

### Logs

```bash
kubectl logs <pod>
kubectl logs -f <pod>
```

---

### Describe

```bash
kubectl describe pod <pod>
```

---

### What to Look For

* Events section
* Errors (image pull, crash)

---

### Example Failure

Wrong image:

```bash
kubectl create deployment bad --image=nginx:wrongtag
```

Check:

```bash
kubectl describe pod <pod>
```

---

### Key Insight

> Always check `describe` before searching online

---

## 12. Self-Healing (Pod Deletion)

### Command

```bash
kubectl delete pod <pod>
kubectl get pods -w
```

---

### Behavior

* Pod deleted
* Controller detects mismatch
* New Pod created automatically

---

### Key Insight

> Kubernetes continuously enforces desired state

---

## 13. Node Drain (Planned Maintenance)

### Command

```bash
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
```

---

### Behavior

* Pods moved to other nodes
* Node marked unschedulable

---

### Use Case

* Hardware maintenance
* Updates

---

### Re-enable Node

```bash
kubectl uncordon <node>
```

---

## 14. Simulating Node Failure

### Action

* Shutdown worker VM

---

### Observe

```bash
kubectl get nodes
```

Node becomes:

```text
NotReady
```

---

### Behavior

* Pods on failed node recreated elsewhere
* Temporary disruption possible

---

### Key Insight

> Distributed systems assume failures will happen

---

## 15. What Kubernetes Is Actually Doing

### Continuous Loop

```text
Desired State (etcd)
      ↓
Controllers + Scheduler
      ↓
Actual State (Pods)
      ↓
Compare → Fix → Repeat
```

---

### Flow

```text
kubectl → API Server → etcd
        → Controllers → Scheduler → Nodes
```

---

### Key Insight

> Kubernetes is an automated SRE continuously fixing your system

---

## Full Demo Script (Instructor Flow)

### Step 1: Cluster Check

```bash
kubectl get nodes
```

---

### Step 2: Deploy

```bash
kubectl create deployment demo-nginx --image=nginx
```

---

### Step 3: Expose

```bash
kubectl expose deployment demo-nginx --type=NodePort --port=80
```

---

### Step 4: Scale

```bash
kubectl scale deployment demo-nginx --replicas=3
```

---

### Step 5: Debug

```bash
kubectl logs <pod>
kubectl describe pod <pod>
```

---

### Step 6: Failure

```bash
kubectl delete pod <pod>
```

---

### Step 7: Node Drain

```bash
kubectl drain <node> --ignore-daemonsets
```

---

### Step 8: Node Failure

* Shutdown VM
* Observe rescheduling

---

## Common Issues and Fixes

### Pod Stuck in Pending

* No resources available
* Scheduler cannot place Pod

---

### Image Pull Error

```bash
kubectl describe pod <pod>
```

---

### Cannot Access Service

* Check NodePort
* Check firewall
* Verify Pods running

---

### Node NotReady

* Network issue
* kubelet down

---

## Key Takeaways

* Kubernetes manages containers across machines
* It operates using a **desired state model**
* It continuously reconciles system state
* It provides:

  * Scheduling
  * Scaling
  * Self-healing
* Failures are expected and handled automatically

---

## Final Mental Model

```text
You define → Kubernetes enforces → System stabilizes
```

