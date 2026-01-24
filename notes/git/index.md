---
layout: page
title: git
permalink: /notes/git/
---

# git

commands i keep looking up.

---

## daily driver

```bash
# new branch
git checkout -b feature/whatever

# interactive staging (best feature)
git add -p

# commit
git commit -m "add thing"

# push (first push on new branch)
git push -u origin feature/whatever
```

## undo mistakes

```bash
# undo last commit, keep changes
git reset --soft HEAD~1

# forgot something? add to last commit
git add forgotten-file
git commit --amend --no-edit

# discard all local changes (CAREFUL)
git checkout -- .
git clean -fd  # untracked files too
```

## rebase (clean history)

```bash
# update branch with current main
git fetch origin
git rebase origin/main

# clean up commits (squash, reword, etc.)
git rebase -i HEAD~3

# if it goes wrong
git rebase --abort
```

## my aliases

in `~/.gitconfig`:

```ini
[alias]
    s = status -sb
    co = checkout
    lg = log --oneline --graph -15
    last = log -1 HEAD --stat
    undo = reset --soft HEAD~1
    yolo = push --force-with-lease
```

`--force-with-lease` instead of `--force` → safer, aborts if remote changed.

## stash

```bash
git stash                    # park changes
git stash push -m "WIP xyz"  # with name
git stash list               # what's there?
git stash pop                # get latest back
```

---

## links

- [pro git book](https://git-scm.com/book/en/v2) – the reference
- [learn git branching](https://learngitbranching.js.org/) – interactive practice
