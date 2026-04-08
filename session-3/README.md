# Distributed Systems and Infrastructure (Proxmox + Real Setup)

## Overview

This section bridges the gap between:

> Running containers on a single machine
> → Running systems across **multiple machines (distributed systems)**

You will understand:

* Why modern systems require multiple machines
* How distributed systems behave
* How real infrastructure is built using virtualization
* How a **Proxmox cluster simulates a cloud environment**
* How all layers (hardware → Kubernetes) fit together

---

## Learning Objectives

By the end of this section, you should be able to:

* Explain what a distributed system is
* Understand scalability, fault tolerance, and availability
* Understand how virtualization is used in real infrastructure
* Map lab infrastructure to cloud equivalents (e.g., AWS EC2)
* Understand the full stack: hardware → Kubernetes
* Reason about real-world infrastructure failures

---

## 1. From Single Machine to Many

### Problem

Running everything on a single machine introduces:

* Resource limits (CPU, RAM, disk)
* Single point of failure
* No scalability

### Transition

To handle real workloads:

> We distribute computation across multiple machines.

---

### Mental Model

```text
Single Machine → Multi-Machine Cluster → Distributed System
```

---

### Key Insight

> Scaling beyond one machine introduces **networking, coordination, and failure complexity**

---

## 2. What Is a Distributed System?

### Definition

A distributed system is:

> A collection of independent computers that work together and appear as a single system to users.

---

### Characteristics

* Multiple nodes (machines)
* Communication over network
* Coordination between components
* Partial failures are expected

---

### Examples

* Search engines
* Streaming platforms
* Banking systems
* Cloud-native applications

---

### Important Clarification

Users should not need to know:

* Which machine handled their request
* Whether a machine failed internally

---

## 3. Why We Need Multiple Machines

### Core Motivations

#### Scalability

* Handle increasing load by adding machines
* Horizontal scaling preferred over vertical scaling

#### Fault Tolerance

* System continues even if some machines fail

#### High Availability (HA)

* System remains accessible with minimal downtime

---

### Real-World Example

Single server handling exam registrations:

* Works for 100 users
* Crashes at 10,000 users

Solution:

* Distribute load across multiple servers

---

### Trade-Off

More machines → more complexity:

* Network failures
* Synchronization issues
* Deployment challenges

---

## 4. Key Distributed Systems Concepts

### Scalability

Ability to grow capacity by adding resources.

### Fault Tolerance

System continues operating despite failures.

### High Availability

System uptime is maximized (e.g., 99.9%).

---

### Analogy

| Concept         | Analogy                         |
| --------------- | ------------------------------- |
| Scalability     | Adding more checkout counters   |
| Fault Tolerance | One counter breaks, others work |
| Availability    | Store remains open consistently |

---

## 5. Virtualization in Real Infrastructure

### Reality

Modern infrastructure does **not** run applications directly on hardware.

Instead:

```text
Hardware → Hypervisor → Virtual Machines → Applications
```

---

### Why Virtualization?

* Isolation between workloads
* Efficient resource utilization
* Multi-tenancy
* Flexibility in deployment

---

### Cloud Parallel

Cloud providers (e.g., AWS):

* Use virtualization internally
* Expose VMs as services (e.g., EC2)

---

## 6. Proxmox: The Lab Infrastructure Platform

### What Is Proxmox VE?

* Open-source virtualization platform
* Combines:

  * KVM (VMs)
  * LXC (containers)
* Provides:

  * Web UI
  * CLI tools
  * Clustering support

---

### Why Use Proxmox?

* Simulates real cloud infrastructure
* Full control over hardware and virtualization
* Ideal for learning distributed systems

---

### Key Insight

> Proxmox = your own private cloud platform

---

## 7. Proxmox Cluster Setup

### Physical Setup

* 3 physical machines (nodes)
* Each runs Proxmox VE directly on hardware

---

### Cluster Properties

* Nodes are interconnected
* Managed as a single unit
* Can host and migrate VMs

---

### Key Insight

> A Proxmox cluster behaves like a small data center

---

## 8. Control Machine and Network Design

### Components

* 1 control machine (Linux Mint)
* 3 Proxmox nodes
* Private network (e.g., 192.168.x.x)

---

### Configuration

* Static IPs assigned to:

  * Nodes
  * VMs
* SSH access enabled across machines

---

### Example Network

```text
Control Machine: 192.168.1.10
Node1:           192.168.1.11
Node2:           192.168.1.12
Node3:           192.168.1.13
VMs:             192.168.1.100+
```

---

### Key Insight

> Predictable networking is essential for distributed systems

---

## 9. VM Design (Ubuntu + Cloud-Init)

### Base Setup

* Ubuntu minimal images
* Cloned from template

---

### Cloud-Init

Automates initial configuration:

* User creation
* SSH keys
* Hostname setup
* Package installation

---

### Example Cloud-Init Config

```yaml
#cloud-config
users:
  - name: dev
    ssh-authorized-keys:
      - ssh-rsa AAAAB3...
    sudo: ALL=(ALL) NOPASSWD:ALL

packages:
  - docker.io
  - curl
```

---

### Key Insight

> Automation is required even in small clusters

---

## 10. Cloud Analogy (AWS Mapping)

| Lab Component   | AWS Equivalent   |
| --------------- | ---------------- |
| Proxmox Node    | Physical host    |
| VM              | EC2 instance     |
| Cloud-init      | User data script |
| Private network | VPC subnet       |

---

### Key Insight

> Your lab mimics real cloud infrastructure concepts

---

## 11. Common Problems (Reality Check)

### Networking Issues

* Incorrect subnet or gateway
* Nodes unable to communicate

---

### SSH Problems

* Missing keys
* Firewall blocking access

---

### Resource Constraints

* Overcommitting CPU/RAM
* VM performance degradation

---

### Cluster Issues

* Node failures
* Quorum loss in Proxmox

---

### Key Insight

> Infrastructure work is largely debugging and system reasoning

---

## 12. Thinking in Layers (System Design View)

### Full Stack

```text
Hardware
  ↓
Proxmox (Hypervisor)
  ↓
Virtual Machines
  ↓
Operating System (Ubuntu)
  ↓
Docker (Container Runtime)
  ↓
Kubernetes (Orchestration)
```

---

### Request Flow

```text
User → Network → Node → VM → Container → Application
```

---

### Key Insight

> Each layer abstracts complexity but adds its own failure modes

---

## 13. Why This Setup Matters

### Benefits

* Realistic cloud-like environment
* Full control over system
* Ability to debug at all layers

---

### Learning Advantage

Compared to managed cloud:

* You understand *why things work*
* Not just *how to use them*

---

## 14. Single Machine vs Cluster

### Single Machine

**Pros**

* Simple
* Easy to debug

**Cons**

* Limited scalability
* Single point of failure

---

### Cluster

**Pros**

* Scalable
* Fault tolerant

**Cons**

* Complex
* Harder to debug
* Network-related failures

---

### Key Insight

> Distributed systems fail in more complex and unpredictable ways

---

## 15. Bridge to Kubernetes

### Current Setup

You now have:

* Multiple physical machines
* Virtual machines on each node
* Docker running inside VMs

---

### Problem

Containers are still:

* Managed manually
* Limited to individual machines

---

### Solution

> Kubernetes orchestrates containers across multiple machines

---

### Transition

Next step:

```text
Docker (single node) → Kubernetes (multi-node orchestration)
```

---

## Supporting Demo (Highly Recommended)

---

## Demo 1: Multi-VM Connectivity

### From Control Machine

```bash
ssh user@192.168.1.11
ssh user@192.168.1.12
```

---

### Verify Communication

```bash
ping 192.168.1.12
```

---

## Demo 2: Run Containers on Multiple VMs

On Node 1:

```bash
docker run -d -p 5001:80 nginx
```

On Node 2:

```bash
docker run -d -p 5002:80 nginx
```

---

### Access

```text
http://192.168.1.11:5001
http://192.168.1.12:5002
```

---

### Insight

* Same container
* Different machines
* No coordination yet

---

## Demo 3: Resource Awareness

### Check Resources

```bash
htop
free -m
```

---

### Observation

* Each VM has limited resources
* Overloading one node affects performance

---

## Demo 4: Failure Simulation

### Stop One Node

```bash
shutdown now
```

---

### Observe

* Services on that node become unavailable
* Other nodes unaffected

---

### Insight

> Distributed systems must handle partial failure

---

## Demo 5: SSH Automation (Optional)

From control machine:

```bash
for ip in 192.168.1.11 192.168.1.12; do
  ssh user@$ip "hostname"
done
```

---

### Insight

* Infrastructure is controlled programmatically
* SSH is foundational for automation

---

## Troubleshooting (Critical Section)

### Cannot SSH

* Check IP
* Check SSH service
* Check firewall

---

### Nodes Not Communicating

```bash
ping <node-ip>
```

---

### High Load / Slow VMs

```bash
top
htop
```

---

### Cluster Issues

* Check quorum
* Verify node connectivity

---

## Key Takeaways

* Distributed systems use multiple machines to scale and survive failures
* Virtualization enables flexible infrastructure
* Proxmox simulates real-world cloud environments
* Infrastructure operates in layers
* Failures are expected and must be handled
* Kubernetes builds on top of this foundation
