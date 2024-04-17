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

Du côté de Bob, étant passif, il ne connait que l'encryption de $x_A$ et $y_A$ et ne peut donc guère obtenir plus d'informations utiles. Cependant, du côté d'Alice, en étant malicieuse passive, elle a la possibilité de déterminer une cercle sur lequel se trouve Bob.

## Question 4

Pour vérifier si Bob est à moins de 100 mètres sans connaitre sa distance, nous lui faisons généré une liste qui contient :$\{a \times b\} \forall a,b \in [0;100]$
pour tous les élements i de la liste (et un élément aléatoire $r_i$), nous calculons :
$(d^2-i)*r_i$
Cette liste est ensuite mélangée. Grâce au mélange et au nombre aléatoire, Alice ne pourra pas déduire la position de Bob.
Alice déchiffrera tous les éléments jusqu'à tomber sur un 0. Quand ce sera le cas, elle pourra déduire que Bob est à moins de 100 mètres. Si elle ne tombe jamais sur un 0, cela nous indique que la distance n'entre pas dans l'intervalle, et donc que Bob est à plus de 100 mètres

## Question 5

Bob étant toujours passif, il ne pourra obtenir aucune information sur Alice. La multiplication par un nombre aléatoire non connu par Alice du côté de Bob en plus du mélange de la liste permet de rendre complètement impossible la récupération d'informations sur la position de Bob du côté d'Alice. La sécurité est donc garantie qu'Alice soit malicieuse passive ou active car la seule chose sur laquelle elle puisse mentir est sa position.

