# Flagship Article Writing Brief

## Locked Story

- Main claim: structured multimodal-to-text representations can support salient-moment detection in long videos under tighter budget constraints than direct video reasoning.
- Research-first framing: the benchmark and the textual representation are the scientific contribution.
- Product-transfer framing is secondary and belongs mainly in thesis discussion, not in the article core.

## Headline Evidence Already Available

- benchmark size: 29 validation pairs
- average source segment duration: about 320.5 s
- average ground-truth clip duration: about 53.5 s
- best complete structured-text run: combined score 0.301
- complete direct-video baseline: combined score 0.273

## Core Claims You Can Already Make

- an end-to-end multimodal-to-text pipeline was built
- the benchmark is reproducible and queryable from SQLite
- the active structured-text stack has full visual-template coverage on the 29 benchmark videos
- a complete structured-text condition is competitive with a complete direct-video baseline on the full validation set

## Claims To Avoid Until More Runs Exist

- no-VLM ablation conclusions on the full benchmark
- model ranking claims based on partial 24/26/27-sample runs
- any headline claim derived from 1-sample or 5-sample smoke runs

## How To Use The Exploratory Runs

- keep them in a dedicated pilot-results table, separate from the full-29 comparison table
- use them to justify design decisions: transcript-only is too weak, several inline or scene-grouped variants help, and `typed-v1` becomes the retained representation before the direct-video comparison
- never compare a 5-sample pilot score to a 29-sample headline score as if they carried the same weight
- use the pilot table to explain iteration logic, not to claim final superiority

## Exploratory Narrative To Write

- start with the cheap pilot strategy explicitly: low-volume runs were used to iterate quickly on representation and prompting before running expensive full-set evaluations
- then explain representation evolution in order: transcript baseline, inline or scene-grouped variants, typed timeline variant, timestamped or tool variants, and the no-VLM ablation
- end the subsection by stating that this exploratory phase narrowed the candidate space and motivated the final full comparison against direct-video input

## Recommended Section Logic

1. Problem and motivation
2. Related work
3. Benchmark construction
4. Preprocessing pipeline
5. Structured textual representation
6. Selector and metrics
7. Full-run results
8. Failure analysis
9. Conclusion

## Minimum Figures

- Figure 1: system overview
- Figure 2: one end-to-end worked example
- Figure 4: success/failure qualitative comparison

## Minimum Tables

- exploratory pilot synthesis
- dataset statistics
- pipeline components
- context variants and size
- main full-29 results only
- failure taxonomy

## Writing Rule

If a number does not come from a full 29-sample run, treat it as exploratory unless you explicitly mark it as pilot evidence.
