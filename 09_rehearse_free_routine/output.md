
`claude -p "summarize yesterday's commits, write to summary.md onto a claude/summary branch" --als "Read,Edit,Bash"`


## Claude's Output:
```
Done. Here's what was created:


It covers the 3 commits from **August 21, 2026**:

| Commit | Description | Files |
|--------|-------------|-------|
| `3adcd16` | feat: break-it-on-purpose project | 6 files (+149 lines) |
| `01e6d4c` | fix: stale TODO/FIXME cleanup | 1 file |
| `244430b` | fix: stale TODO/FIXME cleanup (follow-up) | 1 file |

The branch is ready to push whenever you're set.
```


`claude -p "Read a file called this-file-does-not-exist.md and summarize its contents into a new summary file onto a claude/summary branch." --allowedTools "Read,Edit,Bash"`

## Claude's Output

```
The file `this-file-does-not-exist.md` does not exist in the current directory, so there's nothing to summarize.

If you meant a different file, let me know the correct filename and I'll read and summarize it for you.
```