# Section 2 Exercises

## Exercise 1: First Container

### Task
Run your first container.

```bash
docker run hello-world
````

### Questions

* Why does the container exit immediately?
* What steps does Docker perform internally when running this command?
* Where is the image pulled from?

## Exercise 2: Inspect Containers

### Task

List running and stopped containers.

```bash
docker ps
docker ps -a
```

### Questions

* Why is the hello-world container not visible in `docker ps`?
* What does the STATUS field indicate?
* What is the difference between a running and exited container?

## Exercise 3: Run a Web Server

### Task

Run an nginx container in detached mode.

```bash
docker run -d -p 8080:80 nginx
```

### Questions

* What does `-d` (detached mode) do?
* What does `-p 8080:80` mean?
* Why does this container keep running?

## Exercise 4: Access Application

### Task

Open the application in your browser:

```
http://localhost:8080
```

### Questions

* What response do you see?
* How is the request routed from your browser to the container?
* What happens if you stop the container?

## Exercise 5: View Logs

### Task

Inspect container logs.

```bash
docker logs <container_name>
```

### Questions

* What type of logs are displayed?
* What happens when you refresh the browser multiple times?
* Why are logs critical for debugging?

## Exercise 6: Execute Inside Container

### Task

Enter the container shell.

```bash
docker exec -it <container_name> /bin/sh
```

### Questions

* What does `-it` mean?
* Are you inside the host system or the container?
* What differences do you observe compared to your host environment?

## Exercise 7: Build an Image

### Task

Build a Docker image from a Dockerfile.

```bash
docker build -t myapp:v1 .
```

### Questions

* What is an image?
* What are layers in Docker?
* Why are builds cached?

## Exercise 8: Run Custom Application

### Task

Run your built image.

```bash
docker run -d -p 5000:5000 myapp:v1
```

### Questions

* Why must the application bind to `0.0.0.0`?
* What happens if it binds to `localhost`?
* How does Docker map ports?

## Exercise 9: Container Lifecycle

### Task

Stop and remove a container.

```bash
docker stop <container_name>
docker rm <container_name>
```

### Questions

* Why can't you remove a running container?
* What happens to data stored inside the container?
* Is the image deleted when the container is removed?

## Exercise 10: Volumes

### Task

Create and inspect a volume.

```bash
docker run -v mydata:/data nginx
docker volume ls
```

### Questions

* Where is the volume stored?
* What happens to data after container deletion?
* Why are volumes necessary?

## Exercise 11: Multi-Container Setup

### Task

Run services using Docker Compose.

```bash
docker compose up
```

### Questions

* What problem does Docker Compose solve?
* What does `depends_on` do?
* How do containers communicate with each other?

## Exercise 12: Debugging Failure

### Task

Introduce an error:

* Use a wrong image name
* Use a wrong port

```bash
docker logs <container_name>
docker ps -a
```

### Questions

* What error do you observe?
* How do you identify the root cause?
* Which command is most useful for debugging?

## Exercise 13: Networking Concept

### Scenario

You have two containers:

* App container
* Database container

### Questions

* Can they communicate by default?
* How does Docker networking enable communication?
* What happens if ports are not exposed?

## Exercise 14: Thought Experiment

### Scenario

You need to deploy:

* A web app
* A database
* Persistent storage

### Questions

* How would you structure this using Docker?
* What components need volumes?
* What breaks if containers are removed?
* How would you scale this system?

## Final Check

You should now be able to:

* Run and inspect containers
* Build and run images
* Debug container issues
* Use volumes for persistence
* Run multi-container applications
* Understand Docker networking basics
