# Section 1 Exercises

## Exercise 1: Process Understanding

### Task
List running processes.

```bash
ps aux
````

### Questions

- How many processes are running?
- Which process is consuming the most CPU?
    



## Exercise 2: Resource Contention

### Task

Run a CPU-heavy process (example loop).

```bash
yes > /dev/null
```

### Questions

- What happens to CPU usage?
- How does this affect other processes?
    



## Exercise 3: Isolation Thinking

### Scenario

Two applications require:

- Python 3.8
- Python 3.11
    

### Questions

- Can they run easily on same OS?
- What problems arise?
- How would VMs solve this?
- How would containers solve this?
    



## Exercise 4: VM vs Container Reasoning

### Question

For each scenario, choose VM or container:

1. Running Windows on Linux
2. Running 100 microservices
3. Strong security isolation needed
    
Explain your reasoning.



## Exercise 5: Namespaces Concept

### Question

What happens if:

- A process can see all system processes?
- A process can modify global filesystem?
    

Why is this dangerous?



## Exercise 6: cgroups Concept

### Scenario

One application consumes all RAM.

### Questions

- What happens to other applications?
- How do cgroups solve this?
    



## Exercise 7: Mental Model Check

Answer briefly:

- Is a container a VM?
- Does a container have its own kernel?
- What keeps containers isolated?
    



## Exercise 8: Thought Experiment

Design a system for:

- 1000 users
- Multiple services
- Different dependencies
    

### Questions

- Would you use processes only?
- VMs?
- Containers?
- Why?
    

