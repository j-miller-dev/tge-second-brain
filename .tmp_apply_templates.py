from pathlib import Path
import shutil

root = Path(r'c:\Users\JasonMil\Desktop\notes')
lit_dir = root / 'Literature Notes' / 'Discrete Math'
perm_dir = root / 'Permanent Notes' / 'Discrete Math'
perm_dir.mkdir(parents=True, exist_ok=True)

atomic_files = [
    'additive inverses.md',
    'conditional statements.md',
    'Existential statement.md',
    'Existential Universal Statements.md',
    'Existential-Universal vs Universal-Existential Statements.md',
    'set.md',
    'Universal Conditional Statements.md',
    'Universal Existential Statements.md',
    'Universal statement.md',
]

literature_files = [
    'algorithms and their analysis.md',
    'applications and modeling.md',
    'combinatorics and discrete Probability.md',
    'discrete structures.md',
    'Important types of mathematical statements.md',
    'induction and recursion.md',
    'Logic and Proof.md',
    'mathematical proof.md',
    'mathematical reasoning.md',
    'real numbers.md',
    'spiral approach to concept developmen.md',
    'Variables.md',
    'Writing Sentences Using Variables.md',
]

for name in atomic_files:
    src = lit_dir / name
    dst = perm_dir / name
    if src.exists() and not dst.exists():
        shutil.move(str(src), str(dst))
    elif src.exists() and dst.exists():
        src.unlink()
    if dst.exists():
        title = dst.stem
        content = f'''---
title: {title}
created: 2026-07-17
type: permanent
source:
related_notes:
  - 
tags:
  - discrete-math
  - permanent
---

# {title}

## Core idea
- Add a concise definition or explanation here.

## Why it matters
- Explain why this concept matters in a proof, definition, or argument.

## Short example
- Add a brief example or illustration.

## Related notes
- [[Permanent Notes/Discrete Math/Index]]
'''
        dst.write_text(content, encoding='utf-8')

for name in literature_files:
    path = lit_dir / name
    if not path.exists():
        continue
    title = path.stem
    content = f'''---
title: {title}
created: 2026-07-17
type: literature
source:
related_notes:
  - 
tags:
  - discrete-math
  - literature
---

# {title}

## Source
- Add the lecture, chapter, or book source.

## Main claim
- Add the main point of this note here.

## Key ideas
- Add the central ideas here.

## Important details
- Add definitions, examples, or references here.

## Connection to other notes
- Link to related atomic notes or other literature notes.
'''
    path.write_text(content, encoding='utf-8')

perm_index = perm_dir / 'Index.md'
perm_index.write_text('''# Permanent Notes — Discrete Math

Use this folder for atomic, definition-style notes.

## Good candidates
- Definitions
- Single concepts
- Short proof techniques

## Related
- [[Literature Notes/Discrete Math/Index]]
''', encoding='utf-8')

lit_index = lit_dir / 'Index.md'
lit_index.write_text('''# Discrete Math Literature Notes

Use this folder for broader lecture-style, chapter-style, or topic-style notes.

## Suggested use
- Lecture summaries
- Topic overviews
- Longer explanations

## Related
- [[Permanent Notes/Discrete Math/Index]]
''', encoding='utf-8')
