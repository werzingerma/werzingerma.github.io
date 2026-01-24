---
layout: page
title: Git
permalink: /notizen/git/
---

# Git

Befehle die ich ständig nachschlage.

---

## Daily Driver

```bash
# Neuer Branch
git checkout -b feature/whatever

# Interaktiv stagen (bestes Feature)
git add -p

# Commit
git commit -m "Add thing"

# Push (erster Push auf neuem Branch)
git push -u origin feature/whatever
```

## Fehler rückgängig

```bash
# Letzten Commit undo, Änderungen behalten
git reset --soft HEAD~1

# Was vergessen? Zum letzten Commit hinzufügen
git add forgotten-file
git commit --amend --no-edit

# Alles lokale wegwerfen (VORSICHT)
git checkout -- .
git clean -fd  # auch untracked files
```

## Rebase (clean history)

```bash
# Branch auf aktuellen main bringen
git fetch origin
git rebase origin/main

# Commits aufräumen (squash, reword, etc.)
git rebase -i HEAD~3

# Wenns schiefgeht
git rebase --abort
```

## Meine Aliases

In `~/.gitconfig`:

```ini
[alias]
    s = status -sb
    co = checkout
    lg = log --oneline --graph -15
    last = log -1 HEAD --stat
    undo = reset --soft HEAD~1
    yolo = push --force-with-lease
```

`--force-with-lease` statt `--force` → sicherer, bricht ab wenn remote sich geändert hat.

## Stash

```bash
git stash                    # Änderungen parken
git stash push -m "WIP xyz"  # Mit Name
git stash list               # Was liegt rum?
git stash pop                # Letzten wieder holen
```

---

## GitHub Actions

Für die Portfolio-Seite hab ich das hier:

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: npm run build
      - name: Deploy to Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

---

## Links

- [Pro Git Book](https://git-scm.com/book/en/v2) – die Referenz
- [Learn Git Branching](https://learngitbranching.js.org/) – interaktiv üben
