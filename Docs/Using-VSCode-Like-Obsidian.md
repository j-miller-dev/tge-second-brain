# Using VS Code Like Obsidian

You can use VS Code as a lightweight second-brain workspace even without Obsidian. The key is to treat your Markdown files like interconnected notes.

## 1. Create a note-first workflow

- Make one Markdown file per idea, topic, project, or meeting.
- Keep notes short and focused.
- Use clear headings so notes stay readable.

## 2. Link notes together

Use simple Markdown links between files:

- `[Work Note](Work/Index.md)`
- `[Daily Capture](Inbox/Daily%20Capture.md)`

This works like a basic wiki-style connection system.

## 3. Create backlinks manually

Backlinks are links from one note to another. In VS Code, you can create them by adding links at the bottom of a note such as:

```md
## Related Notes
- [Home](../Home.md)
- [Work Index](../Work/Index.md)
```

This gives you a basic form of backlinking even without Obsidian-specific features.

## 4. Use folders for structure

A simple structure helps a lot:

- Inbox/ for quick capture
- Work/ for work notes
- Kindle/ for reading notes
- Discrete Math/ for study notes

## 5. Use tags in plain text

You can mimic Obsidian-style tags by writing tags as plain text:

```md
#work #reading #math
```

This makes it easy to search and scan notes.

## 6. Use a daily note habit

Create a daily note such as:

- [Templates/Daily Note Template.md](../Templates/Daily%20Note%20Template.md)

Use it to capture:
- tasks
- ideas
- reading notes
- study points
- follow-ups

## 7. Use preview mode for reading

Open the Markdown preview to read notes more clearly.

- Press Ctrl+Shift+V for preview
- Use Markdown Preview Enhanced for a better experience

## 8. Use Git to preserve your knowledge base

Because this is a Git-backed workspace, you can:

- save versions of your notes
- review changes over time
- backup your second brain to a repository

Example:

```bash
git status
git add .
git commit -m "Update notes"
git push
```

## 9. Best practice for working like Obsidian in VS Code

Think of your vault like this:

- capture quickly
- connect related notes
- review regularly
- keep notes small and useful
- link ideas instead of duplicating them

That is the core of a second-brain workflow.
