import numpy as np

# Les états de base, écrits comme des vecteurs
ket0 = np.array([1.0, 0.0])
ket1 = np.array([0.0, 1.0])

# Les portes, écrites comme des matrices
X = np.array([[0.0, 1.0],
              [1.0, 0.0]])
H = np.array([[1.0, 1.0],
              [1.0, -1.0]]) / np.sqrt(2)

def probabilites(etat):
    """Renvoie (P(0), P(1)) pour un état à deux amplitudes réelles."""
    return etat[0] ** 2, etat[1] ** 2

# Test 1 : X transforme |0> en |1>
print("X|0> =", X @ ket0)

# Test 2 : H crée une superposition équilibrée
etat = H @ ket0
print("H|0> =", etat, "-> probabilites :", probabilites(etat))

# Test 3 : H deux fois ramène à |0> (interférence)
etat2 = H @ (H @ ket0)
print("HH|0> =", etat2, "-> probabilites :", probabilites(etat2))