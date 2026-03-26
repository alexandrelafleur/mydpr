# Resume Et Angle Du Memoire

## These Directrice Du Memoire

Le memoire doit revenir plus explicitement a l'axe du DPR: la question principale est de savoir si une representation textuelle de la video permet d'obtenir une qualite de selection comparable, voire superieure, a une approche multimodale directe tout en reduisant fortement les besoins de calcul, de jetons, de cout monetaire et donc de puissance machine. La these generale doit donc etre formulee comme une these de **resource-constrained video understanding**.

La formulation centrale du memoire peut etre la suivante:

> Une representation textuelle structuree de la video peut servir d'alternative competitive a l'analyse video multimodale directe pour la detection de moments saillants, tout en consommant beaucoup moins de ressources et en rendant l'approche plus realiste pour des systemes contraints, notamment en robotique.

Le memoire doit donc defendre en priorite quatre idees:

- l'analyse video multimodale directe reste puissante, mais elle est trop couteuse pour plusieurs contextes reels;
- une representation video-as-text suffisamment riche permet de conserver l'information utile a la selection des moments saillants;
- sur le benchmark actuel, cette approche texte structure obtient un score similaire ou superieur avec beaucoup moins de ressources;
- cette baisse de cout rend l'approche beaucoup plus credible pour des systemes embarques, des usages a fort volume et des pipelines robotiques.

Les chiffres headline doivent servir cette these. Sur le run complet actuel, le contexte texte structure atteint `0.301` contre `0.273` pour l'entree video directe, avec environ `11885` jetons contre `29191`, soit environ `2.46x` moins de jetons et `2.85x` moins de cout. C'est ce genre de message qui doit porter le memoire.

Une deuxieme ligne d'argument, issue de la base historique `test_llms.db`, doit maintenant completer ce message. Elle montre que le deplacement du calcul peut aussi se faire par fine-tuning, mais pas pour n'importe quelle taille de modele: dans une campagne qui a coute environ `1000 USD` en credits Google, `Gemini 2.5 Flash` passe d'environ `0.300` a `0.437` d'IoU moyen apres fine-tuning texte, tout en restant tres peu couteux a l'execution, alors que `Flash-Lite` ne suit pas la meme trajectoire. Cette ligne ne remplace pas la these principale du memoire; elle l'etend. Elle montre qu'un systeme contraint peut soit deplacer la perception vers une representation plus legere, soit deplacer une partie de l'alignement vers une phase amont de fine-tuning, a condition que le modele ait la bonne capacite pour en beneficier.

## Ce Qui Distingue Le Travail

La difference centrale avec les approches multimodales directes est double:

- au niveau du memoire, la representation textuelle sert d'abord a reduire les besoins de calcul sans effondrer la performance aval;
- au niveau de l'article, cette meme representation sert aussi a transformer l'analyse video en donnees structurees que le LLM et le code peuvent manipuler.

Le memoire doit donc expliquer clairement que la video-as-text representation n'est pas seulement une compression pratique. C'est un moyen de deplacer une partie de la perception vers une chaine moins couteuse, afin de rendre l'analyse video faisable sous contrainte, puis de beneficier en plus d'un etat structure reusable.

## Niveaux De Contribution A Rendre Visibles

Le memoire doit montrer au moins cinq couches de contribution:

- une demonstration qu'une approche text-only structuree peut rester competitive face a une entree video directe a cout bien moindre;
- un pipeline multimodal multi-etapes qui deplace la charge de perception vers une representation textuelle exploitable;
- un benchmark dataset reliant des videos YouTube a leurs Shorts pour mesurer la qualite de selection aval;
- une boucle de benchmarking et d'optimisation, avec persistance SQLite, prompt engineering, context engineering et harness d'execution;
- une architecture de representation qui, en plus de reduire les couts, produit un etat video structure, reusable par des LLMs et par du code.

La these generale du memoire peut donc etre formulee ainsi:

> Une bonne representation video-as-text n'est pas seulement une facon moins chere de decrire une video; c'est une facon de rendre l'analyse video assez legere pour des systemes contraints, tout en conservant une structure exploitable pour des traitements plus riches.

## Resume Global De L'Article Central

L'article central peut maintenant porter plus directement l'idee mecaniste et systeme du travail. Il doit montrer qu'en convertissant la video en representation textuelle structuree, on obtient non seulement un contexte de selection efficace, mais surtout un etat video ordonne, persiste, queryable, editable et reusable dans le temps.

Sa question peut etre formulee ainsi:

> Comment une representation video-as-text structuree permet-elle a un LLM text-only de raisonner sur une video, de la reinspecter dans plusieurs sessions et d'alimenter des traitements logiciels plus complexes qu'une simple inference multimodale one-shot?

L'article doit donc documenter tres clairement:

- le pipeline multi-etapes qui transforme la video en artefacts persistants puis en vue textuelle exploitable;
- la representation `typed-v1` comme structure de travail, et non comme simple resume libre;
- la facon dont cette representation peut etre lue par un LLM, reinjectee dans une autre session, interrogee plus finement et manipulee par du code;
- le benchmark `validation29` comme preuve aval que cette structuration conserve une information utile;
- les resultats quantitatifs et qualitatifs qui montrent que ce choix de representation n'est pas seulement elegant, mais effectivement operationnel.

Le role de l'article est donc davantage d'expliquer **pourquoi** cette representation change la nature de l'analyse video, tandis que le memoire insiste davantage sur **pourquoi cela compte** du point de vue du cout et des contraintes machine.

La campagne historique doit etre utilisee dans l'article comme un contrepoint experimental: elle montre que les petits modeles ne reagissent pas tous pareil au fine-tuning. `Flash-Lite` semble trop limite pour apprendre utilement, `Flash` parait au bon niveau de capacite pour en beneficier, et les grands modeles semblent davantage profiter d'un contexte plus riche que d'un fine-tuning texte trop etroit. Cette nuance aide a formuler une conclusion plus generale sur les systemes contraints.

## Hierarchie A Garder Entre Article Et Memoire

Le memoire combine doit garder cette hierarchie:

- le memoire porte la these principale de reduction de cout et de faisabilite sous contraintes de ressources;
- l'article porte davantage la logique de representation video-as-text comme etat structure et reusable;
- le benchmark et la base SQLite rendent la preuve reproductible et mesurable;
- `mecene-clips` montre le transfert produit, sans remplacer la preuve scientifique;
- la discussion generale relie l'ensemble a la robotique, aux systemes embodied et aux usages reels sous contraintes machine.
- la campagne historique sur le fine-tuning sert de pont entre benchmark textuel et strategie systeme, en montrant comment deplacer le calcul soit dans la representation, soit dans l'alignement amont.

## Table Des Matieres De Travail

### Chapitre 1 - Introduction

- Revenir a la these du DPR: performance comparable sous cout bien plus faible
- Poser highlight detection comme tache de validation sous contrainte de ressources
- Annoncer pipeline, representation, benchmark, harness et portee robotique

### Chapitre 2 - Etat de l'art

- Situer highlight detection et temporal localization
- Situer les approches LLM/VLM long-video et leurs limites de cout
- Introduire les representations structurees comme mecanisme d'efficacite et de reusabilite
- Fermer sur la lacune: manque de comparaisons qualite/cout et de representations video-as-text exploitables

### Chapitre 3 - Articulation du memoire combine

- Expliquer pourquoi un seul article suffit pour la preuve centrale
- Distinguer clairement ce que l'article explique sur la representation et ce que le memoire ajoute sur le cout
- Montrer que le benchmark et la base SQLite sont des pieces de contribution a part entiere

### Chapitre 4 - Article central

- Montrer comment la video brute devient etat textuel structure
- Decrire le pipeline complet et la representation finale
- Expliquer pourquoi cette representation peut etre relue, requetee et manipulee dans le temps
- Valider sa pertinence par un benchmark reproductible de selection de moments saillants
- Ajouter une campagne complementaire sur fine-tuning et enrichissement de contexte pour montrer que le compromis qualite/cout depend aussi de la taille du modele

### Chapitre 5 - Discussion generale et transfert

- Recentrer le message du memoire sur le gain qualite/cout sous contraintes de ressources
- Clarifier la portee reelle des resultats et des limites
- Relier le travail a `mecene-clips`, a la robotique et aux systemes embodied
- Expliquer quand il vaut mieux enrichir le contexte et quand il vaut mieux payer un fine-tuning amont

### Chapitre 6 - Conclusion generale

- Repondre a la question de recherche au niveau article et au niveau memoire
- Reprendre les contributions validees: efficacite, pipeline, benchmark, harness, representation
- Ouvrir sur des representations plus riches, plus selectives, et plus transferables
