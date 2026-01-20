---
layout: page
title: Git
permalink: /notizen/git/
---

<p class="pill">Notes · Version Control · GitHub</p>

A collection of Git commands and workflows I use regularly.

### Basic workflow

The commands I use every day:

```bash
# Create a new branch
git checkout -b feature/my-feature

# Stage changes interactively (review what you're adding)
git add -p

# Commit with message
git commit -m "Add feature X"

# Push and set upstream
git push -u origin feature/my-feature
```

### Fixing mistakes

```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Forgot something in last commit
git add forgotten-file.py
git commit --amend --no-edit

# Discard all local changes (careful!)
git checkout -- .

# Revert a specific commit
git revert <commit-hash>
```

### Rebasing

Rebase keeps history clean by applying your commits on top of the latest main:

```bash
# Update your branch with latest main
git fetch origin
git rebase origin/main

# Interactive rebase to clean up commits
git rebase -i HEAD~3

# If conflicts occur
git add .
git rebase --continue
# Or abort
git rebase --abort
```

### Useful aliases

Add to `~/.gitconfig`:

```ini
[alias]
    s = status -sb
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --all
    last = log -1 HEAD --stat
    undo = reset --soft HEAD~1
```

### Stashing

```bash
# Save work in progress
git stash

# Save with a name
git stash push -m "work in progress on feature X"

# List stashes
git stash list

# Apply latest stash
git stash pop

# Apply specific stash
git stash apply stash@{2}
```

---

## GitHub Actions

Automate workflows on push, pull request, or schedule.

### Basic CI workflow

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

### Common triggers

```yaml
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'  # daily at midnight
  workflow_dispatch:  # manual trigger
```

### Matrix builds

Test on multiple versions:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11']
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

---

## GitHub Pages

Host static sites directly from a repository.

### Setup

1. Go to repository Settings → Pages
2. Select source branch (usually `main` or `gh-pages`)
3. Select folder (`/` or `/docs`)

### Jekyll site

GitHub Pages has built-in Jekyll support:

```yaml
# _config.yml
title: My Site
theme: minima
plugins:
  - jekyll-feed
  - jekyll-seo-tag
```

### Custom domain

1. Add `CNAME` file with your domain
2. Configure DNS:
   - A records pointing to GitHub's IPs
   - Or CNAME pointing to `username.github.io`

### Deploy with Actions

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    steps:
      - uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Build
        run: npm run build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy
        uses: actions/deploy-pages@v4
```

---

### Resources

- [Pro Git Book](https://git-scm.com/book/en/v2) - The definitive guide
- [Learn Git Branching](https://learngitbranching.js.org/) - Interactive tutorial
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
