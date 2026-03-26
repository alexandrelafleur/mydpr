# DPR Reuse Map

This memoire workspace is intentionally anchored in the existing DPR material instead of replacing it.

## Directly Reused Repository Assets

- `../udes-genie-these.cls`
- `../plain-fr.bst`
- `../references.bib`
- `../dpr/source/acronymes.tex`

## DPR Source Areas To Reuse While Writing

- `../dpr/source/dpr.tex`, introduction:
  - motivation
  - resource-constrained framing
  - original research question
- `../dpr/source/dpr.tex`, state-of-the-art chapters:
  - long-video highlight detection
  - temporal localization
  - multimodal alignment
  - consumer clipping systems as practical context
- `../dpr/source/dpr.tex`, problem and methodology chapters:
  - problem decomposition
  - four project objectives
  - comparison logic against reference clips

## How The New Thesis Scaffold Uses The DPR

- `source/01-introduction.tex`
  - thesis-form rewrite of the DPR question, objectives, and contributions
- `source/02-etat-art.tex`
  - explicit guide for restructuring the DPR literature review into the thesis literature chapter
- `source/03-articulation.tex`
  - new material not present in the DPR: article-centered combined-thesis justification
- `source/04-*`
  - entirely new article-centered structure required by the protocol
- `source/05-discussion.tex`
  - reinterpretation of the DPR as completed work rather than future work

## Writing Rule

When possible, move text from the DPR into the thesis chapters by:

1. switching from future tense to completed-work tense;
2. deleting proposal language and schedule language;
3. tying each retained claim to current benchmark evidence.
