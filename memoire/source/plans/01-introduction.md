# Chapitre 1 - Introduction

## Mise en contexte et problematique

```text
Structure:
1) Partir du probleme de l'analyse video longue sous contrainte de calcul, de cout et de puissance machine.
2) Expliquer pourquoi les approches multimodales directes restent difficiles a deployer dans des contextes robotiques ou embarques.
3) Introduire la representation video-as-text comme strategie de reduction de cout qui deplace la charge vers un LLM textuel.
4) Poser la detection de highlights comme tache aval concrete pour verifier que cette economie de ressources ne detruit pas la qualite.

Sujets:
Longues videos, contraintes de calcul, cout monetaire, jetons, robotique mobile, systemes embarques, representation textuelle structuree, clipping comme cas de validation.

Figures/Tableaux:
Pas de figure obligatoire ici.

Points notables:
Le memoire doit d'abord etre centre sur la faisabilite sous contraintes de ressources.
La representation reste centrale, mais comme moyen d'obtenir une analyse video moins couteuse sans perdre la capacite de selection.
La portee robotique vient du fait qu'une methode moins gourmande demande moins de puissance machine.
```

## Question de recherche

```text
Structure:
1) Poser la question de recherche au niveau du memoire.
2) Poser ensuite la sous-question plus representationnelle de l'article.
3) Montrer le lien entre fidelite de representation, cout de traitement et performance aval.

Sujets:
Video-as-text, representation structuree, text-only LLM, moment selection, utilite aval, cout, jetons, ressources, contraintes embarquees.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
La bonne formulation est proche de:
"Comment representer une video sous forme textuelle de maniere assez fidele pour qu'un LLM puisse identifier les moments saillants avec une qualite comparable, tout en utilisant moins de ressources qu'une approche multimodale directe?"
La question principale du memoire porte donc d'abord sur le compromis qualite/cout.
L'article pourra ensuite porter davantage la question de la structure reusable de cette representation.
```

## Objectifs du projet de recherche

```text
Structure:
1) Enoncer l'objectif general comme un objectif deja realise.
2) Decliner les objectifs techniques et experimentaux.
3) Relier chaque objectif a un artefact concret du depot.

Sujets:
Architecture de representation, pipeline multimodal, benchmark YouTube -> Shorts, base SQLite, harness d'execution, prompt engineering, context engineering, comparaison qualite/cout.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
Les objectifs ne doivent pas etre ecrits comme dans le DPR.
Ils doivent montrer ce qui a effectivement ete construit:
- une representation textuelle structuree et persistable;
- un pipeline multi-etapes pour l'alimenter;
- un benchmark dataset et un harness reproductible;
- une comparaison explicite entre qualite de selection et ressources consommees.
```

## Contributions originales

```text
Structure:
1) Ouvrir par la contribution principale en efficacite sous contraintes.
2) Donner ensuite les contributions systeme et evaluation.
3) Terminer par la contribution representationnelle plus large et le transfert pratique.

Sujets:
Representation reusable, stockage en base, ordre temporel, interrogeabilite, progressive disclosure, transcription, scene detection, YOLO tracking, face recognition, diarization, active-speaker detection, person association, camera-focus inference, benchmark, harness, `mecene-clips`.

Figures/Tableaux:
Tableau des contributions:
- tableau ecrit directement dans `source/01-introduction.tex`

Points notables:
La contribution principale du memoire est de montrer qu'une representation textuelle structuree peut rester competitive tout en reduisant fortement les ressources necessaires.
La contribution representationnelle plus large existe aussi, mais elle peut etre davantage portee par l'article.
La detection de highlights sert de preuve aval forte de ce compromis qualite/cout.
```

## Plan du document

```text
Structure:
1) Resumer le role de chaque chapitre.
2) Expliquer que l'article valide une question plus etroite que celle du memoire.
3) Montrer comment les autres chapitres elargissent cette validation vers la these complete.

Sujets:
Introduction, etat de l'art, articulation, article, discussion, conclusion.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
Le lecteur doit comprendre des l'introduction la difference entre:
- la these du memoire: rendre l'analyse video faisable sous contraintes de ressources avec une performance competitive;
- la these de l'article: montrer comment la representation video-as-text transforme la video en etat structure exploitable dans le temps.
```
