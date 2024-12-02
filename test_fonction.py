# Écrire une fonction check0to10(t, n) ayant en paramètres une liste t de taille
# quelconque et un entier n. La fonction doit renvoyer un booléen indiquant s'il
# existe une valeur comprise entre 0 et 10 dans les n premiers éléments de la liste t.
# La fonction doit retourner False si la valeur de n est plus grande que la taille de la
# liste.
def check0to10(t, n):
    for i in range(n):
        if 0 <= t[i] <= 10:
            return True
    return False
t = [12, 65, 23, 14, 85, 11, 8, 41, 9, 0, 55, 3]
print(check0to10(t, 3))