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