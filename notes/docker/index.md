---
layout: page
title: docker
permalink: /notes/docker/
---

# docker

container basics and snippets.

---

## commands i always need

```bash
# start container
docker run -it ubuntu bash              # interactive
docker run -d -p 8080:80 nginx          # detached with port

# what's running?
docker ps                                # running
docker ps -a                             # all

# logs
docker logs -f <container>               # follow

# shell into running container
docker exec -it <container> bash

# cleanup
docker system prune -a                   # removes EVERYTHING not running
```

## dockerfile (python)

my standard template:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "main.py"]
```

**tips:**
- `--no-cache-dir` → smaller image
- `slim` instead of `alpine` for python → fewer issues with compiled packages
- copy dependencies BEFORE code → cache doesn't invalidate when only code changes

## multi-stage build

for smaller production images:

```dockerfile
# build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# run
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

result: only nginx + static files, no node.

---

## docker compose

```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app           # for dev: live reload
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```bash
docker compose up -d      # start
docker compose down       # stop
docker compose logs -f    # logs
docker compose exec app bash  # shell
```

## .dockerignore

don't forget:

```
node_modules
__pycache__
.git
.env
*.log
```

---

more: [docker docs](https://docs.docker.com/)
