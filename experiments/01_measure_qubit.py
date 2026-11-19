import numpy as np

alpha, beta = 0.6, 0.8
p0 = alpha**2  # probabilité théorique de mesurer 0 (= 0.36)

rng = np.random.default_rng(seed=42)

for n_shots in [10, 1000, 100000]:
    tirages = rng.random(n_shots)  # n_shots nombres aléatoires entre 0 et 1
    est_zero = tirages < p0  # True si la mesure donne 0, False si elle donne 1
    freq0 = np.sum(est_zero) / n_shots  # fréquence observée de 0
    print(f"n_shots = {n_shots:>6} : frequence de 0 = {freq0:.4f} (theorie : {p0:.4f})")