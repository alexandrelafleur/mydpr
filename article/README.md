# Article Workspace

Ce dossier contient la version autonome de l'article.

## Structure

- `source/`: source de v\'erit\'e de l'article
- `document/`: point d'entree autonome `article.tex`, artefacts et PDF genere

Le m\'emoire r\'eutilise le m\^eme corps d'article via `source/article-body.tex`.

## Compilation

```bash
cd /Users/lafleur/dev/mydpr/article
make pdf
```
