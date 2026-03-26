# DPR Workspace

Ce dossier regroupe le document canonique du DPR.

## Structure

- `source/`: source LaTeX du DPR et ses fichiers directement associes
- `document/`: artefacts de compilation, PDF genere et lien `document/dpr.tex`
- `archive/`: anciennes variantes et sorties historiques conservees a titre d'archive

## Compilation

```bash
cd /Users/lafleur/dev/mydpr/dpr
make pdf
```

La compilation utilise:

- `references.bib` partage depuis la racine du depot
- `plain-fr.bst` partage depuis la racine du depot
- `udes-genie-these.cls` partage depuis la racine du depot
