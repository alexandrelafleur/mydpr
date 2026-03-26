# Chapitre 3 - Articulation du memoire combine

## Pourquoi un memoire combine centre sur un seul article

```text
Structure:
1) Justifier le format retenu.
2) Expliquer pourquoi un seul article suffit pour porter la preuve experimentale centrale.
3) Montrer que les autres chapitres servent a porter la these plus large du memoire.

Sujets:
Memoire combine, article central, representation reusable, benchmark, protocole institutionnel.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
Le format doit apparaitre comme la consequence logique d'une contribution a deux niveaux:
- le memoire porte la these principale sur le compromis qualite/cout sous contraintes de ressources;
- l'article explicite davantage la logique de representation video-as-text comme structure exploitable.
```

## Lien entre l'article, l'infrastructure de representation et l'application

```text
Structure:
1) Expliquer le role de l'infrastructure de benchmark et de persistance.
2) Expliquer le role de l'article comme exposition de la representation et validation quantitative.
3) Expliquer le role du memoire comme lieu de la these qualite/cout.
4) Expliquer le role de `mecene-clips` comme preuve de transferabilite.

Sujets:
SQLite, artefacts persistants, variantes de contexte, harness d'execution, comparaison de cout, validation scientifique, validation de transfert, produit.

Figures/Tableaux:
Pas de figure obligatoire ici.

Points notables:
Le benchmark et la base ne sont pas juste des outils de support.
Ils font partie de la contribution, parce qu'ils rendent l'evaluation reproductible et permettent de mesurer proprement le compromis qualite/cout.
Ils soutiennent aussi l'argument de representation reusable porte davantage par l'article.
```

## Ce que l'article couvre, et ce que le memoire ajoute

```text
Structure:
1) Dire ce que l'article traite directement.
2) Dire ce que le memoire ajoute autour de cet article.
3) Clarifier pourquoi il n'y a pas redondance.

Sujets:
Article: pipeline, representation, persistance, structure exploitable, evaluation highlight detection.
Memoire: these du DPR sur la reduction de cout, articulation qualite/cout, portee pour robotique/embarque, limites plus larges, transfert.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
L'article ne doit pas etre charge de tout raconter.
Le memoire doit ajouter explicitement ce que l'article explique mal ou pas assez:
- la continuite avec le DPR;
- le message principal sur les ressources economisees;
- la pertinence pour des contextes contraints comme la robotique mobile.
```

## Etat actuel des preuves

```text
Structure:
1) Resumer les couches de preuve disponibles.
2) Distinguer infrastructure, exploration, runs complets et transfert.
3) Dire ce que ces preuves permettent d'affirmer au niveau article et au niveau memoire.

Sujets:
Pipeline construit, base SQLite, benchmark `validation29`, pilotes exploratoires, runs complets, ablation controlee, mesures de cout, reutilisation dans `mecene-clips`.

Figures/Tableaux:
On peut renvoyer aux notes de preuve, mais pas de figure obligatoire.

Points notables:
Les chiffres ne sont qu'une partie de la preuve.
Pour le memoire, il faut surtout montrer que le texte structure atteint une performance competitive avec beaucoup moins de ressources.
Pour l'article, il faut aussi montrer que cette representation existe comme artefact standardise, persistable et interrogeable.
```
