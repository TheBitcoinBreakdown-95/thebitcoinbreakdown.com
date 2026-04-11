# Session Save Rules

When the user says "save progress", "#", or "save":

1. Find the nearest WORKLOG.md to the current working directory
2. Read its current contents
3. Apply the update rules below
4. Keep mutable sections concise -- under 30 lines each
5. After updating the worklog, check `git status` for uncommitted changes. If there are any, offer to commit with a suggested message. Do not commit automatically -- wait for the user to confirm or decline.

## Update Rules

### Last Session (overwrite with preservation)
- Before overwriting, copy the current Last Session content into `## Session History` as a new timestamped entry
- Then write the new Last Session summary
- Format for Session History entries: `### YYYY-MM-DD — [brief title]` followed by the content

### Status / Current State (overwrite)
- These reflect the current snapshot -- overwrite freely

### Next / To-Do / Carried Over (append-only)
- **Never delete items** from these sections
- Add new items only
- If an item is completed, mark it done (`- [x]`) but do not remove it
- If the user explicitly says to remove an item, move it to Session History with a note: `(removed: [reason])`

### Session History (append-only, auto-created)
- If `## Session History` does not exist, create it at the bottom of the worklog
- Always append, never delete entries
- **Every 10 entries**, archive: move all Session History entries to `WORKLOG-ARCHIVE.md` (in the same directory), keeping only the most recent 2 entries in the worklog. Create the archive file if it doesn't exist. Prepend archived entries (newest batch on top).

### Protected Sections
- **Never overwrite or delete protected sections.** Protected sections are marked with `<!-- protected -->` or any of these headings:
  - `## Key Data` / `## Key Brand Data`
  - `## Decisions`
  - `## Reference IDs` / `## IDs`
  - Any section explicitly labeled "protected" or "permanent"
- For protected sections: **append only** -- add new entries, never remove existing ones

---

# Check Worklog Rules

When the user says "check worklog", "check worklog and continue", "where was I", or "what's next":

1. Read the nearest WORKLOG.md to the current working directory
2. If the WORKLOG has a `Daily To-Do` field pointing to a master to-do file, read that file too
3. Find all unchecked tasks (`- [ ]`) and determine what's next based on:
   - The `Last Completed` date/task in the WORKLOG
   - Today's date and the schedule in the master to-do
   - Any tasks that are overdue (past their scheduled date but still unchecked)
4. Present to the user:
   - A brief "where you left off" summary (last session, last completed task)
   - Today's specific task(s) from the daily schedule
   - Any overdue tasks that were missed
   - Ask if they want to start on the next task
5. Do NOT update the WORKLOG -- just read and present. Only update when the user says "save".
