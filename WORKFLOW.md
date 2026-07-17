# VS Code Second Brain Workflow

This workspace is designed as a Git-backed note system for work, reading, and study.

## Recommended structure
- Inbox/ - quick capture and fleeting notes
- Literature Notes/ - lecture notes, book notes, and source-based summaries
- Permanent Notes/ - atomic ideas and synthesized insights
- Projects/ - plans, checklists, and trackers
- Work/ - work notes and decisions
- Kindle/ - book highlights and summaries
- Discrete Math/ - domain hub for discrete math study organization
- Templates/ - reusable note scaffolds

## Daily routine
1. Open the workspace in VS Code.
2. Add a quick note in Inbox/.
3. Move source-based notes into Literature Notes/.
4. Extract one idea at a time into Permanent Notes/.
5. Keep active plans in Projects/.
6. Commit changes regularly with Git.

## Note-quality rules
- A literature note should be tied to one source and written in your own words.
- A permanent note should be atomic, self-contained, and linked to related notes.
- A hybrid note is acceptable when a note needs both source context and a concise conceptual point; keep the main idea explicit and avoid overloading it.
- Avoid mixing projects with knowledge notes.

## Git usage
```bash
git status
git add .
git commit -m "Update notes"
git push
```
