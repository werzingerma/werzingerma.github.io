---
layout: page
title: Docker
permalink: /notizen/docker/
---

<p class="pill">Notes · Containers · DevOps</p>

Notes on Docker for containerizing applications.

### Basic concepts

- **Image**: A template for creating containers (like a class)
- **Container**: A running instance of an image (like an object)
- **Dockerfile**: Instructions for building an image
- **Volume**: Persistent storage that survives container restarts
- **Network**: How containers communicate

### Common commands

```bash
# Run a container
docker run -it ubuntu bash

# Run detached with port mapping
docker run -d -p 8080:80 nginx

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop <container-id>

# Remove a container
docker rm <container-id>

# List images
docker images

# Remove an image
docker rmi <image-id>

# Shell into running container
docker exec -it <container-id> bash

# View logs
docker logs -f <container-id>

# Clean up everything
docker system prune -a
```

### Dockerfile

Basic structure for a Python project:

```dockerfile
# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run command
CMD ["python", "main.py"]
```

### Build and run

```bash
# Build image
docker build -t my-app .

# Build with specific Dockerfile
docker build -f Dockerfile.dev -t my-app:dev .

# Run container
docker run -p 8000:8000 my-app

# Run with environment variables
docker run -e DATABASE_URL=postgres://... my-app

# Run with volume mount (for development)
docker run -v $(pwd):/app my-app
```

### Multi-stage builds

Keep images small by separating build and runtime:

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## Docker Compose

Define and run multi-container applications.

### docker-compose.yml

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DATABASE_URL=postgres://db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: secret
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### Compose commands

```bash
# Start all services
docker compose up

# Start in background
docker compose up -d

# Rebuild images
docker compose up --build

# Stop services
docker compose down

# Stop and remove volumes
docker compose down -v

# View logs
docker compose logs -f

# Run command in service
docker compose exec app bash
```

### Development vs Production

```yaml
# docker-compose.yml (base)
services:
  app:
    build: .

# docker-compose.override.yml (dev - auto-loaded)
services:
  app:
    volumes:
      - .:/app
    environment:
      - DEBUG=true

# docker-compose.prod.yml
services:
  app:
    environment:
      - DEBUG=false
```

```bash
# Development (uses override automatically)
docker compose up

# Production
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

---

### .dockerignore

```
node_modules
__pycache__
*.pyc
.git
.env
.venv
dist
build
*.log
```

### Resources

- [Docker Docs](https://docs.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
