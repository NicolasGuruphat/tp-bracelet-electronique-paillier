# TP bracelet

## Question 1

1. Alice envoie $[x_A]$ et $[y_A]$ à Bob
2. Bob envoie $[x^2_B+y^2_B-2(x_Ax_B+y_Ay_B)]$
- il connait $x_B$ et $X_A$, donc il peut effectuer le produit par constante grace aux propiétés homomorphes de Paillier (de même pour y).
- pour les puissances, elles sont effectuées sur des variables non chiffrées qu'il connait, donc il peut effectuer les calculs directement sur ces dernières
$$
Paillier.Encrypt(x^2_B + y^2_B) \times (([X_A^{x_B} \times Y_A^{y_B}])^2)^{-1}
$$
3. Alice retourne $d_{AB}$
- elle déchiffre le message, car tout est chiffré avec sa clé

## Question 2

voir fichier `tp.py`

## Question 3

