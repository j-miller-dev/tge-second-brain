---
# Flashcard block template — paste at the bottom of any Permanent note
# Compatible with the "Obsidian_to_Anki" plugin (Pseudonium).
# Run the plugin's sync command after adding cards; they'll land in your
# `second-brain` Anki deck automatically based on your plugin config
# (set Deck = second-brain once in the plugin settings, not per-card).
---

## Flashcards

START
Basic
Front: <question — one clear thing being tested>
Back: <answer — as short as it can be while still being correct>
Tags: <domain tag, e.g. discrete-math epp>
END

START
Cloze
Text: <a full sentence with the key term hidden, e.g. "A relation is {{c1::transitive}} if aRb and bRc implies aRc">
Back Extra: <optional — context or why this matters>
Tags: <domain tag>
END

<!--
Card-writing rules:
- One fact or one idea per card. If you need "and", split it.
- Prefer Cloze for definitions/terminology; prefer Basic for "explain why" or
  "when would you use X over Y" style questions — those need active recall,
  not just term-matching.
- Never make a card for something you could just look up in 10 seconds if
  wrong (e.g. exact page numbers). Cards are for things worth having in your head.
- Delete the START/END blocks you don't use in a given note — don't leave
  empty templates for the plugin to choke on.
-->
