---
layout: page
title: Docker
permalink: /notizen/docker/
---

# Docker

Container-Basics und Snippets.

---

## Commands die ich immer brauche

```bash
# Container starten
docker run -it ubuntu bash              # interaktiv
docker run -d -p 8080:80 nginx          # detached mit Port

# Was läuft?
docker ps                                # running
docker ps -a                             # alle

# Logs
docker logs -f <container>               # follow

# Rein in laufenden Container
docker exec -it <container> bash

# Aufräumen
docker system prune -a                   # ALLES weg was nicht läuft
```

## Dockerfile (Python)

Meine Standard-Vorlage:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Dependencies zuerst (besseres Caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "main.py"]
```

**Tipps:**
- `--no-cache-dir` → kleineres Image
- `slim` statt `alpine` für Python → weniger Probleme mit compiled packages
- Dependencies VOR Code kopieren → Cache wird nicht invalidiert wenn nur Code sich ändert

## Multi-Stage Build

Für Production Images:

```dockerfile
# Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Run
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

Ergebnis: Nur nginx + static files, kein Node.

---

## Docker Compose

```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app           # für Development: live reload
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
docker compose up -d      # starten
docker compose down       # stoppen
docker compose logs -f    # logs
docker compose exec app bash  # shell
```

---

## .dockerignore

Nicht vergessen:

```
node_modules
__pycache__
.git
.env
*.log
```

---

## Links

- [Docker Docs](https://docs.docker.com/)
