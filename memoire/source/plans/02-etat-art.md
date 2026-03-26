# Chapitre 2 - Etat de l'art

## Detection de moments saillants dans les longues videos

```text
Structure:
1) Situer le probleme dans la litterature highlight detection / temporal localization.
2) Expliquer pourquoi la video longue rend la decision difficile: multiples pics locaux, bornes floues, besoin de contexte global.
3) Poser la selection de moments comme tache aval credible pour evaluer une approche plus legere que l'entree video directe.

Sujets:
Moment localization, highlight detection, temporal IoU, pertinence semantique, longue duree, contexte global, evaluation aval.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
Il faut presenter highlight detection comme une tache de validation exigeante, pas comme le seul horizon intellectuel du memoire.
```

## Raisonnement long-video avec LLM et VLM

```text
Structure:
1) Resumer les approches directes video/LLM/VLM.
2) Reconnaitre leur force de comprehension multimodale.
3) Expliquer leurs limites principales pour le memoire: cout, latence, volume de contexte et difficulte de deploiement sous contraintes machine.

Sujets:
Video-LLaMA, VTimeLLM, VTG-LLM, raisonnement multimodal direct, cout, latence, volume de contexte, deploiement embarque, exploitation imparfaite des longs contextes (`Lost in the Middle`).

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
Il ne faut pas opposer caricaturalement les VLM au travail.
La vraie critique principale pour le memoire est plus concrete: meme un bon raisonnement multimodal direct reste cher et lourd a deployer pour des systemes contraints.
L'article pourra ensuite insister davantage sur la question de persistance et de reutilisation.
Ajouter une mise a jour recente sur le fait qu'un long contexte n'est pas automatiquement bien exploite par le modele.
```

## Representation multimodale vers texte et etats persistants

```text
Structure:
1) Presenter les approches intermediaires de compression ou de textualisation.
2) Introduire l'idee d'une representation video-as-text comme mecanisme de reduction de cout.
3) Ajouter que cette representation peut aussi devenir un etat video persistant et reusable.

Sujets:
Representations intermediaires, compression, textualisation, schemas textuels, stockage en base, etat structure, standardisation, reusabilite.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
Le texte n'est pas ici un simple resume.
Pour le memoire, il faut d'abord montrer qu'il permet une analyse moins couteuse.
Pour l'article, il faut ensuite montrer qu'il produit aussi une representation exploitable par des LLMs et par du code.
```

## Robotique, systemes embodied et analogues pratiques

```text
Structure:
1) Montrer que la question a une pertinence au-dela du clipping.
2) Expliquer le lien avec les systemes embodied et surtout avec les contraintes de calcul des plateformes robotiques.
3) Ajouter ensuite les produits grand public comme analogues pratiques et terrain de transfert.

Sujets:
Robotique, perception embarquee, ressources limitees, cout, traitement hors-ligne, outils de clipping, valeur operationnelle.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
Le memoire doit faire sentir que le clipping est un excellent terrain de mesure pour une these de reduction de cout.
L'article pourra ensuite elargir vers la logique de representation reusable.
```

## Lacune ciblee par le memoire

```text
Structure:
1) Fermer la revue par une lacune precise.
2) Dire ce qui manque dans la litterature actuelle.
3) Enoncer ce que le memoire et l'article apportent chacun.

Sujets:
Manque de comparaison claire entre representation textuelle structuree et entree video directe sous contrainte de cout; manque de benchmark aval reproductible; manque de representations video-as-text assez structurees pour devenir des etats logiciels exploitables; manque de travaux reliant proprement representation, taille du modele, ajustement fin et oubli catastrophique.

Figures/Tableaux:
Pas de figure obligatoire.

Points notables:
La lacune principale du memoire n'est pas seulement "personne ne transforme la video en texte".
La lacune est qu'il manque une comparaison propre montrant qu'une representation textuelle peut rester competitive tout en reduisant les ressources.
L'article pourra pousser plus loin la deuxieme lacune: la manque de representations video-as-text structurees et reutilisables.
Ajouter aussi la mise a jour recente sur l'ajustement fin: donnees bien choisies (`SHED`) et risque d'oubli catastrophique sur les grands modeles.
```
