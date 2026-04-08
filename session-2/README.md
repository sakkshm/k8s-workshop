# Docker Hands-On and Workflow

## Overview

This section transitions from theory to practice. You will interact directly with Docker to:

* Run containers
* Inspect and debug them
* Build your own images
* Understand persistence and networking
* Run multi-container applications

The goal is **operational intuition**, not memorization.

---

## Learning Objectives

By the end of this section, you should be able to:

* Run and inspect containers
* Understand container lifecycle
* Build images using a Dockerfile
* Debug containers using logs and exec
* Persist data using volumes
* Understand basic container networking
* Run multi-container setups using Docker Compose

---

## 1. Installation (High-Level)

### Requirements

* Linux → Docker Engine
* Windows/macOS → Docker Desktop

### Verification

```bash
docker version
docker info
```

### Common Issues

* Permission denied → add user to docker group:

  ```bash
  sudo usermod -aG docker $USER
  ```
* Windows → WSL2 configuration issues
* macOS → virtualization permissions

---

## 2. Running Your First Container

### Command

```bash
docker run hello-world
```

### What Happens Internally

1. CLI sends request to Docker daemon
2. Daemon checks local image cache
3. If missing → pulls from Docker Hub
4. Creates container
5. Executes command
6. Prints output and exits

### Expected Result

A confirmation message indicating Docker is working correctly.

---

## 3. Listing Containers

### Commands

```bash
docker ps       # running containers
docker ps -a    # all containers
```

### Important Columns

* CONTAINER ID
* IMAGE
* STATUS
* PORTS
* NAMES

### Observation

After running `hello-world`:

* `docker ps` → empty
* `docker ps -a` → shows exited container

---

## 4. Running a Long-Lived Container (Nginx)

### Command

```bash
docker run -d -p 8080:80 nginx
```

### Explanation

* `-d` → run in background
* `-p` → map host port to container port

### Access

Open in browser:

```
http://localhost:8080
```

### Verify

```bash
docker ps
```

---

## 5. Inspecting Containers

### Logs

```bash
docker logs <container_id_or_name>
```

### Interactive Shell

```bash
docker exec -it <container> /bin/sh
```

### Notes

* `-it` → interactive terminal
* `exec` runs a new process inside container
* Use `exit` to leave shell

---

## 6. Cleaning Up

### Stop Container

```bash
docker stop <container>
```

### Remove Container

```bash
docker rm <container>
```

### Remove Image

```bash
docker rmi <image>
```

### Tip

```bash
docker ps -a
```

Use this to confirm what exists before deleting.

---

## 7. Writing a Simple Application

### Example: Python Web App

#### `app.py`

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "Hello from Docker container"}')

server = HTTPServer(("0.0.0.0", 5000), Handler)
print("Server running on port 5000...")
server.serve_forever()
```

---

## 8. Writing the Dockerfile

#### `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Key Concepts

* Each instruction creates a layer
* Layers are cached → faster rebuilds
* Deterministic environment

---

## 9. Building the Image

### Command

```bash
docker build -t myapp:v1 .
```

### Output

* Step-by-step build logs
* Image created locally

### Verify

```bash
docker images
```

---

## 10. Running Your Application

### Command

```bash
docker run -d -p 5000:5000 myapp:v1
```

### Access

```
http://localhost:5000
```

### Debug

```bash
docker logs <container>
```

### Key Insight

The same image runs identically across machines.

---

## 11. Volumes (Data Persistence)

### Problem

Containers are ephemeral → data is lost on deletion

### Solution

Volumes

### Example

```bash
docker run -d -v mydata:/data nginx
```

### Commands

```bash
docker volume ls
docker volume inspect mydata
```

### Use Cases

* Databases
* Logs
* File uploads

---

## 12. Networking Basics

### Default Behavior

* Containers use a bridge network

### Port Mapping

```bash
-p host_port:container_port
```

### Container Communication

* Containers on same network can talk via names

### Example

```bash
docker network ls
```

---

## 13. Docker Compose

### Motivation

Managing multiple containers manually is complex.

### Solution

Docker Compose allows defining everything in a YAML file.

---

## 14. Docker Compose Example

### Project Structure

```
app
├── app.py
├── Dockerfile
└── docker-compose.yml
```

### `docker-compose.yml`

```yaml
version: "3.9"

services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - dbdata:/var/lib/postgresql/data

volumes:
  dbdata:
```

### Run

```bash
docker compose up
```

### Expected Behavior

* Both containers start
* App connects to DB via hostname `db`

---

## 15. Suggested Live Demo Flow

### Step-by-Step

1. Run:

   ```bash
   docker run hello-world
   ```

2. Inspect:

   ```bash
   docker ps -a
   ```

3. Run nginx:

   ```bash
   docker run -d -p 8080:80 nginx
   ```

4. Check logs:

   ```bash
   docker logs <container>
   ```

5. Enter container:

   ```bash
   docker exec -it <container> /bin/sh
   ```

6. Build custom app:

   ```bash
   docker build -t myapp:v1 .
   docker run -d -p 5000:5000 myapp:v1
   ```

7. Run Compose:

   ```bash
   docker compose up
   ```

---

## Troubleshooting (Important)

Common issues:

* Port already in use

  ```bash
  lsof -i :5000
  ```
* Permission denied
* Container exits immediately → check logs
* Build errors → check Dockerfile path and context

### Key Insight

Debugging containers is a core skill.
Logs and inspection commands are your primary tools.

---

## Summary

* Docker simplifies container usage
* Containers are lightweight and fast
* Images are reusable and portable
* Volumes persist data
* Networking connects containers
* Docker Compose manages multi-container systems

