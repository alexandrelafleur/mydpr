# Chapitre 6 - Conclusion generale

## Reponse a la question de recherche

```text
Structure:
1) Repondre a la question de l'article.
2) Repondre ensuite a la question plus large du memoire.
3) Donner la nuance essentielle.

Sujets:
Viabilite du texte structure, support principal de selection, reduction de cout, difference avec le one-shot multimodal, representation reusable, role reel du signal visuel, fine-tuning comme deplacement amont du calcul pour les petits modeles, enrichissement de contexte pour les gros modeles.

Figures/Tableaux:
Aucun.

Points notables:
La reponse finale ne doit pas etre trop etroite.
Elle doit ressembler a ceci:
"Oui, une representation textuelle structuree peut servir de support principal a la detection de moments saillants avec une performance comparable ou superieure, tout en reduisant fortement les ressources necessaires par rapport a une entree video multimodale directe."
La nuance importante est:
"Cette efficacite depend de la qualite de la structure, et cette meme structure ouvre ensuite la voie a une comprehension video reusable par des LLMs et par du code."
Ajouter aussi une nuance de strategie de modele:
"Selon la taille du modele et la stabilite de la tache, il peut etre plus judicieux de payer un fine-tuning amont ou, au contraire, de garder un modele general et de mieux lui fournir le contexte. `Flash-Lite` parait trop petit pour vraiment apprendre, `Flash` semble au bon niveau de capacite, et `Pro` profite surtout d'un contexte plus riche."
```

## Contributions validees par le memoire

```text
Structure:
1) Reprendre les contributions du memoire du plus conceptuel au plus applique.
2) Dire lesquelles sont validees directement.
3) Distinguer validation scientifique et transfert pratique.

Sujets:
Reduction des ressources par representation textuelle, architecture video-as-text, stockage interrogeable, pipeline multimodal, benchmark reproductible, harness d'evaluation, comparaison texte vs video, diagnostic sur la textualisation VLM, transfert vers `mecene-clips`.

Figures/Tableaux:
Inclure l'etat des preuves consolidees:
- `generated/notes/evidence_notes.md`

Points notables:
Le memoire valide d'abord une these d'efficacite sous contraintes:
une representation textuelle structuree peut rester competitive en consommant beaucoup moins de ressources.
Il valide aussi un artefact de recherche plus large: une maniere de transformer une video en etat structure exploitable dans le temps.
```

## Perspectives

```text
Structure:
1) Partir des prolongements immediats.
2) Ouvrir ensuite sur la reutilisation multi-taches de la representation.
3) Conclure sur la portee plus large pour les systemes reels.

Sujets:
Fermeture propre des runs, selection du signal visuel, progressive disclosure, nouveaux benchmarks, annotation, edition, recherche, robustesse hors domaine, robotique et systemes embodied.

Figures/Tableaux:
Aucun.

Points notables:
La suite logique du travail est maintenant plus claire:
1) consolider encore le gain qualite/cout;
2) mieux choisir ce qui est expose a chaque tache;
3) tester la meme representation sur des usages plus riches que la seule selection de highlights.
```
