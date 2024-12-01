from math import sqrt
def premier(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):  # On vérifie jusqu'à sqrt(n), +1 pour inclure 5
        if n % i == 0:  # Si n est divisible par i, ce n'est pas premier
            return False
    return True  # Si aucun diviseur n'est trouvé, alors n est premier

# -----------------------------------------------------------------------------

# Exercice 20

def npremier(n) :
    compteur = 0
    i = 2
    while True : 
        if premier(i) :
            compteur += 1
        if compteur == n :
            return i
        i += 1

print(npremier(10))