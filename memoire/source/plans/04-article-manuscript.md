# Chapitre 4 - Article central

## Introduction

```text
Structure:
1) Partir du probleme de l'analyse video longue et du caractere jetable d'une inference multimodale one-shot.
2) Expliquer pourquoi le transcript brut est insuffisant.
3) Poser la representation textuelle structuree comme etat video exploitable par un LLM text-only et par du code.
4) Annoncer le benchmark, le pipeline et la validation sur highlight detection.

Sujets:
Representation reusable, longues videos, text-only LLM, etat video structure, benchmark `validation29`, highlight detection comme evaluation aval, cout comme consequence utile.

Figures/Tableaux:
Figure 1:
- figure ecrite directement dans `/Users/lafleur/dev/mydpr/article/source/article-body.tex`

Points notables:
L'article ne doit pas etre ecrit comme un simple papier d'economie de cout.
Il doit faire sentir que la vraie nouveaute est de convertir la video en etat textuel structure utilisable dans le temps, dans plusieurs sessions et dans des processus logiciels plus complexes.
```

## Travaux connexes

```text
Structure:
1) Replacer le travail dans la litterature de moment localization.
2) Discuter les approches VLM directes et leurs avantages.
3) Introduire les representations intermediaires et persistantes.
4) Fermer sur la lacune exacte visee par l'article.

Sujets:
Highlight detection, VLM long-video, compression multimodale, representations textuelles, persistance, etats logiciels exploitables, limites des longs contextes (`Lost in the Middle`).

Figures/Tableaux:
Aucun.

Points notables:
La litterature doit converger vers une question precise:
comment evaluer une representation textuelle structuree non seulement comme compression, mais comme support de raisonnement reusable, reinspectable et manipulable?
Ajouter dans cette section une mise a jour courte sur le fait que plus de contexte n'aide pas automatiquement si le modele exploite mal les longues sequences.
```

## Benchmark et construction du jeu de donnees

```text
Structure:
1) Decrire `validation29`.
2) Expliquer la logique video source YouTube -> Short / clip de reference.
3) Montrer pourquoi cette tache mesure l'utilite aval de la representation.
4) Montrer pourquoi SQLite rend le benchmark reproductible, inspectable et compatible avec des analyses iteratives.

Sujets:
29 paires, duree moyenne source 320.5 s, duree moyenne GT 53.5 s, YouTube videos, Shorts ou clips de reference, runs, run items, prompts, contextes.

Figures/Tableaux:
Tableau des stats:
- donnees generees: `source/tableaux_et_figures/table_dataset_stats.tex`
- logique LaTeX: `/Users/lafleur/dev/mydpr/article/source/article-body.tex`

Points notables:
Le benchmark ne sert pas seulement a comparer des modeles.
Il sert a mesurer si une representation video-as-text suffisamment structuree conserve une information utile a une tache concrete de comprehension et de selection.
```

## Pipeline de pretraitement multimodal

```text
Structure:
1) Decrire les etapes dans l'ordre d'execution.
2) Distinguer les artefacts intermediaires de la representation finale.
3) Expliquer comment ces artefacts sont persistes et standardises.
4) Montrer que cette decomposition est ce qui rend la reutilisation possible.

Sujets:
Transcription, scene detection, YOLO tracking, face recognition, diarization, active-speaker detection, person association, camera-focus inference, descriptions VLM, persistance SQLite.

Figures/Tableaux:
Figure 1 si elle n'a pas deja ete introduite.
Tableau des composantes:
- tableau ecrit directement dans `/Users/lafleur/dev/mydpr/article/source/article-body.tex`

Points notables:
Le pipeline ne produit pas juste "plus de texte".
Il construit un etat intermediaire explicable et reusable a partir duquel plusieurs vues textuelles peuvent etre derivees, reinspectees et exploitees par du code.
```

## Representation textuelle structuree

```text
Structure:
1) Presenter `timeline-scenes-dialogue-typed-v1` comme vue canonique de l'etat video.
2) Expliquer ce qu'elle conserve: ordre temporel, scenes, dialogue, personnes, indices visuels.
3) Expliquer pourquoi elle doit etre ordonnee, queryable et compatible avec la progressive disclosure.
4) Distinguer la representation generale de la vue specifique envoyee au selectionneur.

Sujets:
Ordre temporel, scenes, dialogue, descriptions visuelles, structure stable, stockage en base, relecture, reutilisation inter-LLM, acces par code, progressive disclosure, inflation du contexte, variantes exploratoires.

Figures/Tableaux:
Tableau des variantes:
- donnees generees: `source/tableaux_et_figures/table_context_variants.tex`
Figure 2:
- blocs generes: `source/tableaux_et_figures/figure_worked_example.tex`
- logique LaTeX: `/Users/lafleur/dev/mydpr/article/source/article-body.tex`

Points notables:
Dire explicitement que la representation n'est pas une prose libre mais une structure de travail.
Il faut aussi insister sur ce qui la differencie d'un usage VLM one-shot:
elle peut etre inspectee, annotee, tronquee, enrichie, re-injectee dans une autre session LLM et manipulee sans recomputation complete de toute la video.
```

## Configuration du selectionneur et metriques d'evaluation

```text
Structure:
1) Decrire la condition headline.
2) Decrire la baseline video directe.
3) Decrire l'ablation controlee.
4) Expliquer le harness experimental: contextes, prompts, profils, executions, mesures.
5) Expliquer text IoU, temporal IoU et score combine.

Sujets:
Prompt outille, modele Gemini, run headline Grok, harness SQLite, exploration de contextes, comparaison controlee, politique failed=0, retry cible du no-VLM.

Figures/Tableaux:
Aucun tableau obligatoire ici, mais renvoi vers la table de resultats juste apres.

Points notables:
Le harness et le contexte engineering ne sont pas secondaires.
Ils font partie de la contribution, car ils rendent la representation testable, comparable, optimisable et exploitable dans le temps sur plusieurs executions.
```

## Resultats quantitatifs

```text
Structure:
1) Raconter les pilotes exploratoires comme boucle d'optimisation.
2) Donner ensuite la comparaison headline sur les runs complets.
3) Donner enfin l'ablation controlee.
4) Ajouter la campagne historique `test_llms.db` pour montrer l'effet du fine-tuning et du contexte sur d'autres variantes Gemini.
5) Commenter le cout, le volume de jetons et ce qu'ils signifient pour la valeur pratique de la representation.

Sujets:
Transcript baseline, progres exploratoires, `typed-v1` retenu, `0.301` vs `0.273`, `0.315 no-VLM` vs `0.240 with VLM` vs `0.273 direct video`, campagne complementaire sur les 29 cas avec Gemini 2.5 Flash / Flash-Lite / Pro, impact de l'ajustement fin, investissement amont d'environ 1000 USD, cas des objets comme premier essai d'injection visuelle, selection de donnees pour l'ajustement fin (`SHED`), oubli catastrophique sur les grands modeles.

Figures/Tableaux:
Pilotes:
- `source/tableaux_et_figures/table_exploratory_context_runs.tex`
- `source/tableaux_et_figures/table_exploratory_milestones.tex`
Headline:
- `source/tableaux_et_figures/table_main_full_runs.tex`
Ablation controlee:
- `source/tableaux_et_figures/table_controlled_gemini_ablation.tex`
Fine-tuning petits modeles:
- `source/tableaux_et_figures/table_llm_small_finetuning.tex`
Premiere augmentation objets:
- `source/tableaux_et_figures/table_llm_object_augmentation.tex`
Comparaison Gemini 2.5 Pro:
- `source/tableaux_et_figures/table_llm_pro_variants.tex`

Points notables:
Le headline quantitatif doit rester present, mais comme validation aval.
Mais le sens profond des resultats doit etre:
la qualite vient d'une representation mieux structuree et mieux exploitable, pas d'une simple verbalisation massive du visuel.
Et cette structuration produit quelque chose qu'une inference multimodale jetable ne produit pas: un etat video durable.
La campagne historique doit ajouter une nuance essentielle:
- `Flash-Lite` semble trop petit pour vraiment apprendre la tache via fine-tuning;
- `Flash` semble etre au bon niveau de taille pour en beneficier fortement;
- `Pro` semble trop puissant pour tirer profit d'un fine-tuning texte etroit, et profite davantage d'un contexte plus riche.
Ces trois points doivent etre relies a des travaux recents sur les longs contextes, la selection des donnees d'ajustement fin et l'oubli catastrophique.
```

## Analyse des echecs et discussion

```text
Structure:
1) Montrer les succes pour etablir que la representation soutient un vrai raisonnement.
2) Analyser les echecs typiques.
3) Relier ces echecs a la calibration de la representation et non seulement au choix du modele.

Sujets:
Mauvaises frontieres temporelles, pics locaux voisins, surcharge descriptive, ambiguite de hierarchisation, signal visuel mal textualise, besoin de zoom local, besoin de vues plus selectives.

Figures/Tableaux:
Taxonomie:
- tableau ecrit directement dans `/Users/lafleur/dev/mydpr/article/source/article-body.tex`
Figure 4:
- blocs generes: `source/tableaux_et_figures/figure_success_failure.tex`
- logique LaTeX: `/Users/lafleur/dev/mydpr/article/source/article-body.tex`

Points notables:
Cette section doit renforcer la these de l'article:
si le systeme echoue, c'est souvent parce que la bonne information n'est pas encore transmise avec la bonne forme ou la bonne granularite.
Les resultats historiques sur les objets et sur Gemini 2.5 Pro doivent etre mobilises ici pour montrer que cette idee depasse le seul benchmark principal:
la question n'est pas "plus de contexte" en general, mais "quel contexte ce modele sait-il reellement exploiter?".
```

## Conclusion

```text
Structure:
1) Repondre a la question de l'article.
2) Dire ou se trouve la vraie valeur de la methode.
3) Donner la suite logique des travaux.

Sujets:
Viabilite de la voie texte-d'abord, representation reusable, structure temporelle/scenique/dialoguee, limites de la textualisation VLM actuelle, fine-tuning des petits modeles comme deplacement du cout vers l'amont, besoin de contexte plus riche plutot que de fine-tuning texte pour les gros modeles.

Figures/Tableaux:
Aucun.

Points notables:
La conclusion visee est:
1) oui, une representation textuelle structuree peut soutenir la detection de highlights;
2) la vraie contribution de l'article est de rendre la comprehension video reusable et instrumentable;
3) la suite logique est de mieux choisir le signal visuel a transmettre, pas d'ajouter du texte sans discipline;
4) et, selon la taille du modele, de choisir entre enrichissement du contexte et fine-tuning amont plutot que de supposer qu'une seule strategie convient partout.
```
