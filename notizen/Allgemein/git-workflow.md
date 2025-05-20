---
layout: page
title: Git-Workflow Best Practices
permalink: /notizen/Allgemein/git-workflow/
---

# Git-Workflow Best Practices

*Letzte Aktualisierung: 18.05.2025*

Diese Notiz enthält meine persönlichen Best Practices für die Arbeit mit Git und GitHub, die ich mir im Laufe der Zeit angeeignet habe.

## Grundlegende Git-Befehle

```bash
# Repository klonen
git clone https://github.com/username/repository.git

# Status überprüfen
git status

# Änderungen stagen
git add <datei> # oder git add . für alle Änderungen

# Commit erstellen
git commit -m "Aussagekräftige Commit-Nachricht"

# Änderungen pushen
git push origin <branch>

# Änderungen pullen
git pull origin <branch>

# Neuen Branch erstellen und wechseln
git checkout -b <neuer-branch>

# Zu existierendem Branch wechseln
git checkout <branch>