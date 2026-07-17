# Note-Taking & Flashcards for Discrete Math (Epp + MIT 6.1200J)

Discrete math is proof-heavy. Rote flashcards ("what's the definition of X") only cover the shallowest layer — you can know every definition and still freeze on a proof. This guide splits the workflow so both layers get built deliberately.

## Step 1 — Process each chapter/lecture into a Literature note

One Literature note per chapter (Epp) or per lecture (6.1200J), titled e.g. `Epp Ch4 — Elementary Number Theory` or `6.1200J L03 — Graph Theory Basics`.

In your own words, capture:
- What problem is this section actually solving? (Not "what does it cover" — what breaks if you don't know this?)
- The key definitions, stated plainly.
- The 1-2 theorems/techniques that matter most.
- One worked example, reconstructed from memory after closing the book — if you can't, that's a flag you don't understand it yet, not a note-taking failure.

## Step 2 — Extract Permanent notes

Not everything becomes a Permanent note — only ideas you could explain to someone else right now. Good candidates from a discrete math source:

- **A single technique**, e.g. `Proof by Contradiction Assumes the Negation Then Finds an Inconsistency`
- **A single definition with its "why"**, e.g. `A Bijection Is Injective and Surjective — Why Both Matter for Counting`
- **A single connecting insight**, e.g. `Induction Is Just Recursion Run in the Proof Direction` — these cross-domain links (to your dev curriculum) are the highest-value notes you'll write in this whole track.

Skip a Permanent note for anything that's purely mechanical (e.g. "how to compute nCr") — that belongs on a flashcard, not as a standalone idea.

## Step 3 — Split flashcards into two tiers

### Tier 1 — Recall cards (definitions, notation, small facts)
Use the Cloze format from the flashcard template. These exist so notation and terminology stop being a tax on your working memory during a proof.

Examples:
- "A graph is {{c1::bipartite}} if its vertices can be split into two sets with no edges within a set."
- "The {{c1::pigeonhole principle}} states that if n items are put into m containers with n > m, at least one container holds more than one item."

### Tier 2 — Technique cards (the actual hard part)
Use Basic format. The question should force you to *reconstruct a strategy*, not recall a fact. Answer should be the outline of a proof approach, not the full proof.

Examples:
- Front: "How would you prove a statement is false for all n using strong induction — what's the actual structure?"
  Back: "Assume P(k) true for all k < n, show P(n) follows — the strength is you get to use *every* prior case, not just n-1."
- Front: "You're asked to count arrangements where order doesn't matter and repeats aren't allowed — which technique?"
  Back: "Combinations, nCr — recognise 'order doesn't matter, no repeats' as the trigger phrase."

Technique cards are worth more per card than recall cards. If you're short on time, prioritise these.

## Step 4 — The actual test (ties back to the Mastery Checklist)

Don't mark a discrete math concept "mastered" in your checklist until you can do this, unaided:
- State the definition (Tier 1 — should be automatic by now)
- Explain *why* the technique works, not just *that* it works
- Apply it to a problem you haven't seen before

Flashcards get you through step 1 fast so you can spend your actual thinking time on steps 2 and 3 — that's the whole point of separating recall from technique.

## Topic map (for structuring your MOC)

Create a `Discrete Math MOC` note linking out to Literature + Permanent notes under these headings, matching Epp's structure and 6.1200J's lecture order:

- Logic & Proof Techniques (direct proof, contradiction, contrapositive, induction, strong induction)
- Sets, Relations & Functions (relations, equivalence relations, bijections)
- Number Theory (divisibility, modular arithmetic, GCD, basics of cryptography)
- Counting & Combinatorics (permutations, combinations, pigeonhole, binomial theorem)
- Graph Theory (graphs, trees, connectivity, Euler/Hamiltonian paths)
- Recurrences & Asymptotics (solving recurrences, Big-O formally)
- Probability (as covered in 6.1200J's later lectures — random variables, expectation)

As each Literature note gets written, add it under the matching heading. The gaps in that list, visually, are your actual study plan for what's left.
