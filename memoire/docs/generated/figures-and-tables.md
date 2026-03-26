# Plan Des Figures Et Tableaux

Ce document sert de guide de production visuelle pour le m\'emoire et l'article. Il ne remplace pas les figures finales, mais il fixe le message que chaque figure doit faire passer, les donn\'ees \`a mobiliser et l'endroit naturel o\`u l'ins\'erer.

## Figure 1 — Vue D'ensemble Du Pipeline

- Emplacement naturel: article, section `Pipeline de pr\'etraitement multimodal`
- Message \`a faire passer:
  - la d\'ecision finale est textuelle
  - le texte est aliment\'e par une extraction multimodale locale
  - le pipeline est modulaire et explicable
- Contenu recommand\'e:
  - segment source
  - transcription / diarisation
  - d\'ecoupage en sc\`enes
  - personnes visibles / locuteurs / focus cam\'era
  - descriptions VLM
  - contexte `typed-v1`
  - LLM s\'electionneur
  - span pr\'edit
- Forme recommand\'ee:
  - diagramme horizontal ou vertical \`a blocs
  - chaque bloc avec une courte sortie textuelle
  - diff\'erencier en couleur les \'etapes audio, vision et structuration texte

## Figure 2 — Exemple De Transformation Vid\'eo Vers Texte

- Emplacement naturel: article, section `Repr\'esentation textuelle structur\'ee`
- Message \`a faire passer:
  - la repr\'esentation finale n'est pas un r\'esum\'e vague
  - elle conserve assez d'information pour guider la s\'election
- Cas recommand\'es:
  - `6O3MzPeomqs-H4-0h_iDWME`
  - `0qz1ZKR4hkE-43_ki2v9WIQ`
- Source utile:
  - [figure_worked_example.tex](/Users/lafleur/dev/mydpr/memoire/source/tableaux_et_figures/figure_worked_example.tex)
- Contenu recommand\'e:
  - id du sample
  - dur\'ee du segment source
  - extrait du contexte `typed-v1`
  - clip GT
  - clip pr\'edit
  - courte note expliquant pourquoi le cas est r\'eussi
- Forme recommand\'ee:
  - mise en page en trois colonnes
  - colonne 1: m\'etadonn\'ees
  - colonne 2: extrait de contexte
  - colonne 3: comparaison GT / pr\'ediction

## Figure 3 — Positionnement DPR / Article / Produit

- Emplacement naturel: chapitre `Discussion g\'en\'erale et transfert`
- Message \`a faire passer:
  - le DPR a formul\'e l'hypoth\`ese
  - l'article apporte la validation scientifique
  - `mecene-clips` porte la validation de transfert
- Contenu recommand\'e:
  - bloc 1: question du DPR
  - bloc 2: benchmark + article
  - bloc 3: transfert vers le produit
  - sous chaque bloc: type de preuve
- Forme recommand\'ee:
  - frise ou diagramme \`a trois blocs
  - fl\`eches simples
  - une phrase maximum par bloc

## Figure 4 — Cas De Succ\`es Et D'\'echec

- Emplacement naturel: article, section `Analyse des \'echecs et discussion`
- Message \`a faire passer:
  - les erreurs sont interpr\'etables
  - le syst\`eme rate souvent la fronti\`ere ou le pic local, pas toujours le sujet g\'en\'eral
- Cas de succ\`es recommand\'es:
  - `6O3MzPeomqs-H4-0h_iDWME`
  - `0qz1ZKR4hkE-43_ki2v9WIQ`
  - `VIU8WAFixWs-LsORe5wtHzM`
- Cas d'\'echec recommand\'es:
  - `9ByjCwumwBM-xSiFAXHE-mI`
  - `VMUt82uYCd8--cHI7WOC2PQ`
  - `I8LPZc9WJLw-bB6sxbF-Bcw`
- Contenu recommand\'e:
  - span GT
  - span pr\'edit
  - text IoU
  - temporal IoU
  - type d'\'echec selon la taxonomie
- Forme recommand\'ee:
  - grille 2 x 3
  - rang\'ee 1 = succ\`es
  - rang\'ee 2 = \'echecs

## Figure 5 — Co\^ut Versus Qualit\'e

- Statut: optionnelle mais utile
- Message \`a faire passer:
  - la condition texte structur\'e ne se contente pas d'\^etre comp\'etitive
  - elle d\'eplace le compromis qualit\'e / co\^ut
- Source utile:
  - [table_main_full_runs.tex](/Users/lafleur/dev/mydpr/memoire/source/tableaux_et_figures/table_main_full_runs.tex)
  - [table_exploratory_context_runs.tex](/Users/lafleur/dev/mydpr/memoire/source/tableaux_et_figures/table_exploratory_context_runs.tex)
- Forme recommand\'ee:
  - nuage de points
  - axe x = co\^ut ou tokens
  - axe y = score combin\'e
  - couleur = type de condition

## Table 1 — Correspondance Des Contributions

- Emplacement:
  - [01-introduction.tex](/Users/lafleur/dev/mydpr/memoire/source/01-introduction.tex)
- Usage:
  - introduction

## Table 2 — Statistiques Du Benchmark

- Donn\'ees inject\'ees:
  - [table_dataset_stats.tex](/Users/lafleur/dev/mydpr/memoire/source/tableaux_et_figures/table_dataset_stats.tex)
- Logique LaTeX:
  - [article-body.tex](/Users/lafleur/dev/mydpr/article/source/article-body.tex)
- Message:
  - benchmark petit mais bien d\'efini

## Table 3 — Composantes Du Pipeline

- Emplacement:
  - [article-body.tex](/Users/lafleur/dev/mydpr/article/source/article-body.tex)
- Message:
  - la repr\'esentation finale est le produit d'une cha\^\i ne multimodale explicable

## Table 4 — Variantes De Contexte

- Donn\'ees inject\'ees:
  - [table_context_variants.tex](/Users/lafleur/dev/mydpr/memoire/source/tableaux_et_figures/table_context_variants.tex)
- Logique LaTeX:
  - [article-body.tex](/Users/lafleur/dev/mydpr/article/source/article-body.tex)
- Message:
  - le budget de contexte est une variable de premier ordre

## Table 5 — Synth\`ese Des Pilotes Exploratoires

- Donn\'ees inject\'ees:
  - [table_exploratory_context_runs.tex](/Users/lafleur/dev/mydpr/memoire/source/tableaux_et_figures/table_exploratory_context_runs.tex)
- Logique LaTeX:
  - [article-body.tex](/Users/lafleur/dev/mydpr/article/source/article-body.tex)
- Message:
  - expliquer pourquoi `typed-v1` a \'et\'e retenu
  - montrer que les pilotes racontent l'it\'eration m\'ethodologique
- R\`egle de r\'edaction:
  - toujours pr\'esenter cette table comme `pilote`
  - ne jamais la m\'elanger aux revendications principales

## Table 5b — Jalons D'am\'elioration Exploratoire

- Donn\'ees inject\'ees:
  - [table_exploratory_milestones.tex](/Users/lafleur/dev/mydpr/memoire/source/tableaux_et_figures/table_exploratory_milestones.tex)
- Logique LaTeX:
  - [article-body.tex](/Users/lafleur/dev/mydpr/article/source/article-body.tex)
- Usage:
  - optionnelle
  - utile si tu veux raconter l'ordre des changements de repr\'esentation

## Table 6 — Conditions Compl\`etes Retenues

- Donn\'ees inject\'ees:
  - [table_main_full_runs.tex](/Users/lafleur/dev/mydpr/memoire/source/tableaux_et_figures/table_main_full_runs.tex)
- Logique LaTeX:
  - [article-body.tex](/Users/lafleur/dev/mydpr/article/source/article-body.tex)
- Message:
  - seule table \`a utiliser pour la revendication principale

## Table 7 — Taxonomie Des \'echecs

- Emplacement:
  - [article-body.tex](/Users/lafleur/dev/mydpr/article/source/article-body.tex)
- Message:
  - l'analyse qualitative est structur\'ee et pas seulement impressionniste
