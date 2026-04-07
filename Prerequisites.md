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

Install WSL2 with Ubuntu:

https://learn.microsoft.com/en-us/windows/wsl/install

Ensure WSL version is 2:

```bash
wsl --status
````

### macOS

Use Docker Desktop.



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



### Verification

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


## 8. Notes

- No Kubernetes setup is required beforehand.
- No Proxmox or virtualization setup is required from participants.
- All infrastructure demonstrations will be conducted live.



## 9. Troubleshooting

If Docker fails to run:

```bash
sudo systemctl status docker
```

If permission issues occur:

```bash
newgrp docker
```

Ensure all setup steps are completed before attending the session.