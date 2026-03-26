# Chapitre 5 - Discussion generale et transfert

## Retour sur le DPR

```text
Structure:
1) Rappeler la promesse initiale du DPR.
2) Montrer ce qui a ete reellement construit.
3) Expliquer que le coeur du memoire reste bien la these du DPR sur la reduction de cout, tout en ayant revele une contribution representationnelle supplementaire.

Sujets:
Passage du futur au realise, benchmark concret, pipeline local, representation persistante, discipline methodologique.

Figures/Tableaux:
Aucun.

Points notables:
Il faut dire explicitement que le projet confirme l'intuition initiale de reduction de cout.
Il faut ensuite ajouter que ce travail a aussi revele une contribution plus large: la representation produite devient un etat reusable.
```

## Portee des resultats actuels

```text
Structure:
1) Separer infrastructure, exploration, headline et diagnostic controle.
2) Dire ce que les chiffres autorisent au niveau article.
3) Dire ce qu'ils autorisent au niveau memoire.

Sujets:
Pilotes, run headline complet, ablation Gemini, utilite aval, comparaison qualite/cout, qualite de representation, comprehension reusable, campagne `test_llms.db`, ajustement fin amont, petits vs gros modeles, contexte riche vs alignement etroit, limites d'exploitation des longs contextes.

Figures/Tableaux:
Reference naturelle a:
- `generated/notes/evidence_notes.md`

Points notables:
La these generale du memoire doit rester:
"le texte structure peut faire aussi bien ou mieux avec beaucoup moins de ressources."
Le benchmark mesure cette efficacite aval.
L'article ajoute ensuite que cette meme representation produit aussi un etat exploitable pour des usages plus riches.
La discussion generale doit maintenant ajouter une consequence systeme:
selon la taille du modele et la stabilite de la tache, il peut etre rationnel de payer un fine-tuning amont plutot que de mobiliser en continu un modele plus lourd.
Ancrer cette lecture avec `Lost in the Middle`, `SHED` et les travaux sur l'oubli catastrophique.

## Enseignements complementaires sur le fine-tuning

```text
Structure:
1) Introduire la base historique `test_llms.db` comme campagne complementaire.
2) Montrer d'abord le cas positif du fine-tuning sur Gemini 2.5 Flash.
3) Montrer ensuite les limites: Flash-Lite semble trop petit pour apprendre, Pro texte perd, Pro objets remonte.
4) Tirer la conclusion robotique et systeme.

Sujets:
Investissement amont d'environ 1000 USD, petits modeles specialises, amortissement sur tache frequente, difference entre alignement fin et enrichissement de contexte, grandes architectures qui profitent davantage du contexte, selection des donnees d'ajustement fin, oubli catastrophique.

Figures/Tableaux:
- `source/tableaux_et_figures/table_llm_small_finetuning.tex`
- `source/tableaux_et_figures/table_llm_pro_variants.tex`
- `source/tableaux_et_figures/table_llm_object_augmentation.tex`
- `generated/notes/llm_campaign_notes.md`

Points notables:
La these a faire ressortir est triple:
1) il existe un seuil de capacite minimal pour que le fine-tuning soit utile;
2) `Flash` semble etre dans ce bon regime de taille, alors que `Flash-Lite` reste trop petit;
3) pour un grand modele, un contexte plus riche semble preferable a un fine-tuning texte trop etroit.
```
```

## Lien avec l'application de production

```text
Structure:
1) Identifier ce qui a ete transfere vers le produit.
2) Expliquer pourquoi ce transfert est important pour la these.
3) Maintenir la distinction entre preuve scientifique et preuve de transfert.

Sujets:
Stack canonique du runtime, API de selection de moments, pipeline de clips, stockage de representations, reutilisation dans `mecene-clips`.

Figures/Tableaux:
Figure 3:
- figure ecrite directement dans `source/05-discussion.tex`

Points notables:
Le transfert doit illustrer que la representation est suffisamment standardisee pour etre reprise par un vrai systeme logiciel.
Cela renforce l'argument de reusabilite, mais aussi l'argument pratique du memoire:
une approche moins couteuse et plus structuree a plus de chances d'etre effectivement deployee dans un systeme reel.
```

## Limites et menaces a la validite

```text
Structure:
1) Limites du benchmark.
2) Limites du corpus.
3) Limites de la representation actuelle.
4) Limites de validite externe.

Sujets:
29 paires, biais clip consommateur, un seul aval principal, sensibilite au prompt, risque de bruit descriptif, generalisation robotique, limites des mesures de cout, incomplete exploitation de la progressive disclosure.

Figures/Tableaux:
Aucun.

Points notables:
Il faut dire que le gain qualite/cout observe est prometteur mais encore etabli sur un benchmark limite.
Le memoire doit rester prudent:
la these de reduction de ressources est bien soutenue, mais sa generalisation a d'autres domaines et a la robotique doit encore etre testee plus largement.
```

## Travaux futurs

```text
Structure:
1) Fermer proprement les quelques runs encore imparfaits.
2) Mieux selectionner le signal visuel et les vues textuelles.
3) Etendre ensuite les usages et les domaines.

Sujets:
Runs 29/29 propres, compression de contexte, progressive disclosure, requetes plus fines, representations plus selectives, benchmark plus large, autres taches d'annotation/edition/recherche, donnees plus proches de la robotique.

Figures/Tableaux:
Aucun.

Points notables:
La priorite future est double:
1) consolider encore le compromis qualite/cout;
2) montrer que la meme representation peut aussi servir a plusieurs formes de raisonnement, de selection, d'annotation et d'action.
```
