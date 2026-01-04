# Git Workflow Cheat Sheet for WorldSMEGraphs

> **Quick Reference**: Common Git commands and workflows  
> **Important**: Never use `git commit` or `git push` directly - use **report_progress** tool

## ⚠️ Critical Rule

**DO NOT** commit or push manually in Copilot sessions:
```bash
# ❌ DON'T DO THIS
git commit -m "message"
git push

# ✅ DO THIS INSTEAD
# Use report_progress tool which handles commit and push automatically
```

## Checking Status

### See What Changed
```bash
git --no-pager status
```

### See Actual Changes
```bash
git --no-pager diff
```

### See Changes in Specific File
```bash
git --no-pager diff path/to/file
```

### See Staged Changes
```bash
git --no-pager diff --cached
```

## Viewing History

### Recent Commits
```bash
git --no-pager log --oneline -10
```

### With File Names
```bash
git --no-pager log --oneline --name-only -5
```

### Specific File History
```bash
git --no-pager log --oneline -- path/to/file
```

### View Specific Commit
```bash
git --no-pager show COMMIT_HASH
```

### View Commit with Diff
```bash
git --no-pager show COMMIT_HASH --stat
```

## Branches

### List Branches
```bash
git branch -a
```

### Current Branch
```bash
git branch --show-current
```

### Switch Branch
```bash
git checkout branch-name
```

### Create and Switch
```bash
git checkout -b new-branch-name
```

## Reverting Changes

### Discard Changes in File (NOT COMMITTED)
```bash
git checkout -- path/to/file
```

### Discard All Unstaged Changes
```bash
git checkout -- .
```

### Unstage File (After `git add`)
```bash
git restore --staged path/to/file
```

### View File from Different Commit
```bash
git --no-pager show COMMIT:path/to/file
```

### Restore File from Previous Commit
```bash
git checkout COMMIT_HASH -- path/to/file
```

## Finding Things

### Find Commits Containing Text
```bash
git log --all --grep="search term"
```

### Find Commits Changing Specific File
```bash
git log --all -- path/to/file
```

### Find When Text Was Added
```bash
git log -S "search text" --source --all
```

### Find Commits by Author
```bash
git log --author="name"
```

### Find Commits in Date Range
```bash
git log --since="2026-01-01" --until="2026-01-04"
```

## Comparing

### Compare Branches
```bash
git --no-pager diff main..feature-branch
```

### Compare Commits
```bash
git --no-pager diff COMMIT1..COMMIT2
```

### Show Files Changed Between Commits
```bash
git --no-pager diff --name-only COMMIT1..COMMIT2
```

### Compare with Remote
```bash
git --no-pager diff origin/main
```

## Stashing (Temporary Save)

### Save Current Changes
```bash
git stash push -m "description"
```

### List Stashes
```bash
git stash list
```

### Apply Last Stash
```bash
git stash pop
```

### Apply Specific Stash
```bash
git stash apply stash@{0}
```

### Delete Stash
```bash
git stash drop stash@{0}
```

## Remote Operations

### Fetch Latest
```bash
git fetch origin
```

### See Remote Branches
```bash
git branch -r
```

### See Remote URL
```bash
git remote -v
```

## Common Workflows

### Before Starting Work
```bash
# 1. Check current state
git --no-pager status

# 2. See what branch you're on
git branch --show-current

# 3. Fetch latest changes
git fetch origin
```

### During Work (Check Progress)
```bash
# 1. See what you've changed
git --no-pager status

# 2. View actual changes
git --no-pager diff

# 3. Use report_progress tool to commit (DON'T use git commit)
```

### After Mistakes
```bash
# Discard changes in one file
git checkout -- path/to/file

# Discard all changes
git checkout -- .

# Go back to specific version of file
git checkout COMMIT_HASH -- path/to/file
```

### Checking Recent Work
```bash
# See last 5 commits
git --no-pager log --oneline -5

# See what was in last commit
git --no-pager show HEAD

# See previous commit
git --no-pager show HEAD~1
```

## Useful Aliases

Add to `~/.gitconfig`:

```ini
[alias]
  st = status
  co = checkout
  br = branch
  ci = commit
  unstage = restore --staged
  last = log -1 HEAD
  lg = log --oneline --graph --decorate --all
  show-names = show --name-only
  diff-names = diff --name-only
```

Then use:
```bash
git st        # instead of git status
git lg        # pretty log graph
git last      # show last commit
```

## Troubleshooting

### "Detached HEAD" State
```bash
# Get back to branch
git checkout main  # or your branch name
```

### Accidentally Staged Files
```bash
# Unstage all
git restore --staged .

# Unstage specific file
git restore --staged path/to/file
```

### See What Would Be Committed
```bash
git --no-pager diff --cached
```

### Check If File Is Tracked
```bash
git ls-files path/to/file
```

### Find Large Files in History
```bash
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {print substr($0,6)}' | \
  sort -n -k 2 | \
  tail -10
```

## Common Mistakes & Fixes

### Mistake: Edited Wrong File
```bash
git checkout -- wrong-file.md
```

### Mistake: Want to Undo Last Commit (NOT PUSHED)
```bash
# Keep changes, just undo commit
git reset --soft HEAD~1

# Discard changes too
git reset --hard HEAD~1
```

### Mistake: Need File from 5 Commits Ago
```bash
git checkout HEAD~5 -- path/to/file
```

### Mistake: Merge Conflict
```bash
# See conflicted files
git --no-pager status

# After resolving, mark as resolved
git add resolved-file.txt

# Continue (if during rebase)
git rebase --continue
```

## .gitignore Patterns

Common patterns for WorldSMEGraphs:

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
.pytest_cache/

# Editor
.vscode/
.idea/
*.swp
*~

# OS
.DS_Store
Thumbs.db

# Build artifacts
dist/
build/
*.log

# Temporary
/tmp/
*.tmp
```

## Quick Reference Commands

```bash
# Current status
git --no-pager status

# What changed
git --no-pager diff

# Recent commits
git --no-pager log --oneline -10

# Discard changes
git checkout -- path/to/file

# View commit
git --no-pager show COMMIT_HASH

# Find text in commits
git log --all --grep="search"
```

---

**Remember**: 
- Always use `git --no-pager` to avoid interactive pagers
- Never use `git commit` or `git push` - use **report_progress** tool
- Check `git status` frequently
- Commits are saved automatically by report_progress

**Full Documentation**: 
- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [CI-CD.md](../CI-CD.md)

**Last Updated**: 2026-01-04
