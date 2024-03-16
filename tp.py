from sympy import mod_inverse, randprime
from random import *
from math import sqrt

def getprime(k):
	p = randprime(2**(k-1), 2**k)
	return p


def genkeys(k):
    p = getprime(k)
    q = getprime(k)
    while (p==q):
        q = getprime(k)

    N = int(p * q)
    Phi = int( N - p - q +1)
    return [N, mod_inverse(N, Phi)]


def encrypt(m, pk):
    r = randint(0, pk - 1)
    # print(r)
    N2 = pk*pk
    c= (((1+(m*pk)) * pow(r, pk, N2))) % N2
    return int(c)

def decryptplus(c, pk, sk):
    N2 = pk*pk
    r = (pow(c, sk, pk))
    # print(r)
    s = pow(r, -pk, N2)
    # s = mod_inverse(r, pk)
    # print(f"Exp {s * r % pk}")
    m = int((((c * s) % N2 - 1) % N2) // pk) % N2
    return int(m), r

def decrypt(c, pk, sk):
    m, _ = decryptplus(c, pk, sk)
    return int(m)

alice_pk, alice_sk = genkeys(300)
def step_1(x_alice, y_alice, alice_pk):
    # Réalisée par Alice
    X_alice = encrypt(x_alice, alice_pk)
    Y_alice = encrypt(y_alice, alice_pk)
    return X_alice, Y_alice

def step_2(X_alice, Y_alice, x_bob, y_bob, alice_pk):
    # Réalisée par Bob
    alice_pk_2 = alice_pk * alice_pk

    left_part = encrypt(pow(x_bob, 2) + pow(y_bob, 2), alice_pk)
    computed = pow(
        (
        pow(
            X_alice, x_bob, alice_pk_2
        )
        *
        pow(
            Y_alice, y_bob, alice_pk_2
        ))
        % alice_pk_2, 2, alice_pk_2
    )
    right_part = mod_inverse(computed, alice_pk_2)
    D_AB_part = (right_part * left_part) % alice_pk_2

    return D_AB_part

def step_3(D_AB_part, x_alice, y_alice,alice_pk, alice_sk):
    # Réalisée par Alice
    return sqrt((decrypt(D_AB_part, alice_pk, alice_sk)+x_alice**2+y_alice**2) % alice_pk)
     
# SCOPE Alice (ce que Alice voit)
x_alice = randint(0, 200)
y_alice = randint(0, 200)

# SCOPE Bob (ce que Bob voit) en plus de alice_pk
x_bob = randint(0,200)
y_bob = randint(0,200)

X_alice, Y_alice = step_1(x_alice, y_alice, alice_pk)
D_AB_part = step_2(X_alice, Y_alice, x_bob, y_bob, alice_pk)

# d_ab = step_3(D_AB_part, X_alice, Y_alice, alice_pk, alice_sk)
d_ab = step_3(D_AB_part, x_alice, y_alice, alice_pk, alice_sk)

print(f"xA{x_alice}, yA {y_alice}, xB {x_bob}, yB {y_bob}, d {d_ab}, verif {sqrt((x_bob-x_alice)**2+(y_bob-y_alice)**2)}")
