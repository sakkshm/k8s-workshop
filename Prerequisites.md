# Kubernetes Workshop – Prerequisites

This document outlines the required system setup to ensure a smooth experience during the workshop:

"Kubernetes in Action: Hands-on Exploration on Real Hardware"

Participants are expected to complete the setup before attending.


## 1. Basic Knowledge Requirements

Participants should be comfortable with:

- Basic command-line usage (cd, ls, mkdir, cat)
- Running and installing software from terminal
- Basic understanding of processes and programs
- Familiarity with Linux is helpful but not mandatory


## 2. System Requirements

Minimum:

- OS: Linux / macOS / Windows (with WSL2)
- RAM: 8 GB (16 GB recommended)
- CPU: 4 cores recommended
- Storage: At least 10 GB free space


## 3. Operating System Setup

### Linux (Recommended)

Ubuntu, Linux Mint, or Fedora.



### Windows

#### Step 1: Install WSL2

Open PowerShell as Administrator and run:

```powershell
wsl --install
````

Restart your system after installation.

Verify:

```bash
wsl --status
```

Ensure:

- Default Version: 2
    



#### Step 2: Install Ubuntu

If not installed automatically:

```powershell
wsl --install -d Ubuntu
```

Launch Ubuntu and complete setup (username/password).



### macOS

No additional OS setup required.

Proceed to Docker installation.

## 4. Docker Installation

Docker will be used extensively during the hands-on session.



### Linux (Ubuntu)

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
```

Add current user to docker group:

```bash
sudo usermod -aG docker $USER
```

Reboot or re-login after this step.



### Windows (Docker Desktop + WSL2)

#### Step 1: Install Docker Desktop

Download:

[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Install and ensure:

- "Use WSL2 instead of Hyper-V" is enabled
    



#### Step 2: Enable WSL Integration

- Open Docker Desktop
    
- Go to Settings → Resources → WSL Integration
    
- Enable for your Ubuntu distribution
    



#### Step 3: Verify

Open Ubuntu (WSL terminal):

```bash
docker --version
docker run hello-world
```



### macOS (Docker Desktop)

#### Step 1: Install Docker Desktop

Download:

[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Install `.dmg` and move Docker to Applications.



#### Step 2: Start Docker

Open Docker Desktop and wait until engine is running.



#### Step 3: Verify

```bash
docker --version
docker run hello-world
```



### Verification (All Platforms)

```bash
docker --version
docker run hello-world
```

The second command should run successfully without errors.

## 5. Required Tools

### Git

```bash
sudo apt install git -y
```

Verify:

```bash
git --version
```



### Code Editor (Recommended)

Install any code editor:

- VS Code
    
- Sublime Text
    
- Vim / Neovim
    

## 6. Network Requirements

- Stable internet connection
    
- Ability to pull Docker images (no restrictive firewall)
    

Optional but recommended:

- Basic understanding of ports (e.g., 3000, 8080)
    

## 7. Pre-Workshop Verification

Ensure the following commands work:

```bash
docker run hello-world
docker ps
docker images
git --version
```

All commands should execute without errors.

## 8. Notes

- No Kubernetes setup is required beforehand.
    
- No Proxmox or virtualization setup is required from participants.
    
- All infrastructure demonstrations will be conducted live.
    

## 9. Troubleshooting

### Docker not running

Linux:

```bash
sudo systemctl status docker
```

Start if needed:

```bash
sudo systemctl start docker
```



### Permission issues (Linux)

```bash
newgrp docker
```



### Windows issues

- Ensure Docker Desktop is running
    
- Restart WSL:
    

```powershell
wsl --shutdown
```



### macOS issues

- Restart Docker Desktop
    
- Ensure Docker icon shows engine running
    



Ensure all setup steps are completed before attending the session.