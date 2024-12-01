# 19.Écrire une fonction premier(n) ayant en paramètre un entier et qui renvoie un
# booléen True si l'entier est premier et False sinon. 
from math import sqrt
def premier(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt( n )) + 1):
        if n % i == 0:
            return False
        return True
    
print(premier(10))

# print(int(2**0.5) + 1)