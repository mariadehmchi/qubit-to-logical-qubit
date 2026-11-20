17/11/2026
premier jour 
 19/11/2026 — Mise en place du projet et première simulation de mesure

 Travail réalisé
- Création de l'environnement virtuel `.venv` et installation de `numpy`, `scipy` et `matplotlib`
### Prédiction avant exécution (`01_measure_qubit.py`)
- État testé : alpha = 0,6, beta = 0,8 (normalisé car 0,6^2 + 0,8^2 = 1).
- Probabilité théorique de mesurer |0 : P(0) = |alpha|^2 = 0,36(soit 36%), et P(1) = |beta|^2 = 0,64 (soit 64%).
- Attente : avec `n_shots = 10`, la fréquence observée risque de s'écarter nettement de `0.3600` ; avec `1000` et surtout `100000` mesures, elle devrait se rapprocher de `0.3600` (la fluctuation statistique diminuant en 1/\sqrt{N}).

### Observations après exécution (`seed=42`)
- `n_shots = 10` : la fréquence empirique de `0` est la plus sensible aux fluctuations aléatoires (échantillon très petit), l'écart par rapport à `0.3600` est donc visible.
- `n_shots = 1000`: la fréquence se rapproche déjà nettement de `0.3600`, avec un écart beaucoup plus faible qu'à 10 tirs.
- `n_shots = 100000`: la fréquence est très proche de `0.3600` (à quelques millièmes près), illustrant concrètement la loi des grands nombres.

### Interprétation physique et ingénierie
- Un tirage unique ou un petit nombre de mesures ne révèle pas directement la probabilité théorique : il faut répéter l'expérience (*shots*) pour estimer la distribution de mesure.
- Cette logique de répétition et d'incertitude statistique sera la même lorsqu'on passera à des simulations plus lourdes (matrices densité, bruit, simulation sur GPU) ou à des mesures sur du matériel quantique réel.
Pour P(0) = 0,3600, j'obtiens 0,3640 à 1 000 tirs (écart 0,0040) et 0,3585 à 100 000 tirs (écart 0,0015), conformément à la décroissance de l'incertitude en 1/√n.
La fréquence empirique converge vers la probabilité théorique quand le nombre de mesures augmente, tout en gardant de petites fluctuations aléatoires.
 Ma prédiction pour les trois affichages de 02_gates.py :
 X|0> : échange les amplitudes de |0> = (1.0, 0.0), donc on attend (0.0, 1.0) (soit |1>).H|0> : crée une superposition équilibrée (1/√2, 1/√2) = (0.7071, 0.7071), avec des probabilités (0.5, 0.5).HH|0> : appliquer H deux fois de suite ramène par interférence à |0> = (1.0, 0.0), avec des probabilités (1.0, 0.0).
 ### Observations — Portes X et Hadamard (`02_gates.py`)
- `X|0>` donne `[0. 1.]` (`|1>`), conforme à la prédiction (inversion de l'état de base).
- `H|0>`donne `[0.70710678 0.70710678]` (`1/√2`), avec des probabilités d'environ `0.5` (`0.4999999999999999` à cause de l'arrondi flottant `float64`)[cite: 1, 2].
- `HH|0>` ramène à `[1.00000000e+00 2.23711432e-17]`, soit `|0>` avec une probabilité `~1.0` (`0.9999999999999996`) et une probabilité résiduelle de `5.00e-34` (interférence constructive sur `|0>`, destructive sur `|1>`, aux erreurs d'arrondi numérique près).
