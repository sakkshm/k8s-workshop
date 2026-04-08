# Section 3 Exercises

## Exercise 1: From Single Machine to Multiple Machines

### Scenario
You are running an application on a single machine.

### Questions

- What happens if the machine crashes?
- What happens if traffic suddenly increases?
- Why is a single machine a limitation?



## Exercise 2: Distributed System Basics

### Scenario

A system runs on 3 machines.

### Questions

- How do these machines communicate?
- What challenges arise compared to a single machine?
- What happens if one machine becomes unreachable?



## Exercise 3: Scalability Thinking

### Scenario

Your application usage increases from 100 users to 10,000 users.

### Questions

- What is vertical scaling?
- What is horizontal scaling?
- Which approach is better for modern systems and why?



## Exercise 4: Fault Tolerance

### Scenario

One server in your system crashes.

### Questions

- What happens to users connected to that server?
- How can the system continue functioning?
- What design decisions improve fault tolerance?



## Exercise 5: High Availability

### Scenario

Your system must achieve 99.9% uptime.

### Questions

- What does 99.9% uptime mean in real time?
- What strategies can improve availability?
- Why is redundancy important?



## Exercise 6: Virtualization in Practice

### Task

List all VMs on your Proxmox cluster (or conceptually think if not available).

### Questions

- Why do we use VMs instead of running apps directly on hardware?
- What benefits does virtualization provide?
- What is the overhead of virtualization?



## Exercise 7: Proxmox Cluster Understanding

### Scenario

You have a 3-node Proxmox cluster.

### Questions

- What happens if one node fails?
- What is the benefit of clustering?
- How does this compare to a cloud provider?



## Exercise 8: Network Design

### Scenario

Your setup uses a private network (e.g., 192.168.x.x).

### Questions

- Why use private IPs?
- What is the role of static IPs?
- What happens if IPs change frequently?



## Exercise 9: SSH and Remote Access

### Task

Connect to a VM using SSH.

```bash
ssh user@<vm-ip>
````

### Questions

* Why is SSH preferred for remote management?
* What are SSH keys and why are they used?
* What happens if SSH is misconfigured?

## Exercise 10: Cloud-Init and Automation

### Scenario

You need to create 10 identical VMs.

### Questions

* Why is manual setup inefficient?
* What does cloud-init automate?
* What happens if configurations are inconsistent?

## Exercise 11: Resource Planning

### Scenario

You deploy too many VMs on a node.

### Questions

* What happens when CPU is overcommitted?
* What happens when RAM is exhausted?
* How can you prevent resource contention?

## Exercise 12: Failure Scenarios

### Scenario

A node goes offline due to network issues.

### Questions

* How does the system detect failure?
* What happens to workloads on that node?
* How can systems recover automatically?

## Exercise 13: Layered Architecture

### Task

Understand the stack:

* Hardware
* Proxmox
* VM
* OS
* Docker
* Kubernetes

### Questions

* What does each layer provide?
* What breaks if one layer fails?
* Why is abstraction important?

## Exercise 14: Single Machine vs Cluster

### Scenario

Compare:

* One powerful server
* Three smaller servers

### Questions

* Which is easier to manage?
* Which is more fault tolerant?
* Which scales better?

## Exercise 15: Real-World Debugging

### Scenario

Your system is not working correctly.

Possible issues:

* Network misconfiguration
* SSH failure
* VM not starting

### Questions

* How do you identify the problem layer?
* What tools would you use?
* Why is debugging distributed systems harder?

## Exercise 16: Thought Experiment

### Scenario

Design a mini cloud system with:

* 3 physical servers
* 10 VMs
* Multiple applications

### Questions

* How would you distribute workloads?
* How would you handle failures?
* How would you monitor the system?

## Final Check

You should now understand:

* Why distributed systems exist
* How multiple machines work together
* Role of virtualization in real infrastructure
* Challenges of networking, failures, and scaling
* Layered system design from hardware to containers


