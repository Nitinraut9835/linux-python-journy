# Day 05 – Docker Fundamentals

## What Problem Docker Solves

“It works on my machine” problem caused by:
- Different OS
- Different dependencies
- Different environment variables
- Different runtime versions

Docker packages:
- Application
- Dependencies
- Environment
- Configuration

Into a portable unit called a container.

---

## Key Concepts

### Image
Blueprint or template used to create containers.

### Container
Running instance of an image.

Image = Class  
Container = Object (instance)

---

## Container vs VM

### VM
- Full OS
- Heavy
- Slow startup
- High resource usage

### Container
- Shares host kernel
- Lightweight
- Fast startup
- Efficient

---

## Basic Docker Commands

### Install Docker
sudo apt update
sudo apt install docker.io

### Enable Docker
sudo systemctl enable docker
sudo systemctl start docker

### Test Docker
sudo docker run hello-world

---

## Working with Nginx Container

### Pull Image
sudo docker pull nginx

### Run Container
sudo docker run -d -p 8080:80 nginx

- -d → run in background
- -p HOST_PORT:CONTAINER_PORT

8080 → host machine  
80 → inside container

Access:
http://localhost:8080

---

## Networking Concept

By default:
Docker binds to 0.0.0.0 (all interfaces).

If bound to:
127.0.0.1 → accessible only locally.

External access requires:
- Open firewall port
- Correct IP address
- Network accessibility
