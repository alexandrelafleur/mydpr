# Memoire Workspace

Ce dossier contient le memoire principal.

## Structure

- `document/memoire.tex`: source canonique du memoire et point d'entree de compilation
- `document/`: artefacts de compilation et PDF genere
- `source/`: chapitres, pages liminaires et plans `.md`
- `source/tableaux_et_figures/`: fichiers `.tex` generes, un par tableau ou figure pilotee par les bases
- `generated/notes/`: notes de synthese generees pour la redaction
- `scripts/`: extraction des preuves, regeneration des vues et compilation
- `docs/`: documentation de travail et aide-memoires

Important:

- la logique LaTeX des tableaux et figures vit dans les fichiers de `source/` et dans le corps partage de l'article;
- les fichiers de `source/tableaux_et_figures/` sont generes par les scripts, mais ne servent qu'a injecter des donnees ou des blocs deja prets dans les environnements LaTeX.

## Compilation

```bash
cd /Users/lafleur/dev/mydpr/memoire
./scripts/refresh-thesis-evidence.sh --pdf
```

Si tu veux seulement regenerer les donnees sans recompiler le PDF:

```bash
cd /Users/lafleur/dev/mydpr/memoire
./scripts/refresh-thesis-evidence.sh
```

Equivalents avec `make`:

```bash
cd /Users/lafleur/dev/mydpr/memoire
make refresh
make refresh-pdf
```

Si `latexmk` n'est pas disponible:

```bash
cd document
pdflatex memoire.tex
bibtex memoire
pdflatex memoire.tex
pdflatex memoire.tex
```

## Sources de donnees

Les donnees generees proviennent de:

- `/Users/lafleur/dev/mecene-clips/benchmark/data/benchmark.sqlite3`
- `/Users/lafleur/dev/mydpr/memoire/data/test_llms.db`

Les scripts n'executent pas de nouveaux benchmarks. Ils consolident seulement l'etat courant en:

- fichiers `.tex` generes, un par tableau ou figure reliee aux bases
- notes courtes pour la redaction

Pour la campagne historique sur l'ajustement fin de Gemini, le flux met aussi a jour les vues de reporting dans `memoire/data/test_llms.db` avant de regenerer les fragments.

## Reste a faire

- Replace figure placeholders with final diagrams and plots if the shared article source changes.
- Confirm the one-article combined format with supervisor/faculty.
- Execute the missing full-29 benchmark conditions when ready with `scripts/run_canonical_benchmarks.sh`.
