# GitHub Tricks

## Undoing a Pushed Commit

### 1. Brute Force (Overwrites History – Use with Caution)

```bash
git log --oneline      # View commit history in short form to find the commit hash
git reset --hard <commit_hash>   # Reset local branch to chosen commit, discarding newer commits
git push --force       # Force push to remote to overwrite history
```

⚠️ Only use on personal branches; this deletes commits permanently on remote if others depend on them.

### 2. Safe Way (Recommended – Preserves History)

```bash
git log --oneline      # View commit history to find the commit hash to revert
git revert <commit_hash>  # Creates a new commit that undoes the specified commit
git push               # Push the new revert commit to remote safely
```

✅ Safe for shared branches because it does not rewrite history.

**Best Practices**

- Pull latest changes before undoing. # Avoid conflicts and overwriting others’ commits
- Prefer `git revert` on main/master. # Maintains commit history
- Communicate with your team if using force push. # Prevent surprises or conflicts
- Use feature branches for experiments. # Isolate work and reduce risk