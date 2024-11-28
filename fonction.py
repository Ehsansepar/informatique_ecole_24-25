# --- Importation des modules python ---


# --- Définition des fonctions ---

# Exercice 1

def somme(liste) :
    total = 0 
    # i = 0
    # while i < len(liste) :
    #     total += liste[i]
    #     i += 1
    
    for nbr in range(len(liste)) :
        total += liste[nbr]
    return total
# -----------------------------------------------------------------------------

# Exercice 2

def pair(nbr) :
    if nbr % 2 == 0 :
        return True 
        ...
    elif nbr % 2 == 1 : 
        return False

# -----------------------------------------------------------------------------

# Exercice 3

def maximum(n1, n2, n3) :
    max = 0

    # if n1 < n2 :
    #     return n2
    # elif n2 < n3 :
    #     return n3
    # else :
    #     return n1

    lst = [n1, n2, n3]

    maxi = 0

    for i in range(len(lst)) : 
        if lst[i] > maxi :
            maxi = lst[i]
    
    return maxi

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Example 1
    # l = [5, 8, 9, 47, 36, 123, 5, 3, 1]
    # somme(l) # retournera 237.
    
    # ------------------------------------------

    # Example 2 
    # print(pair(3)) # retournera 0
    # print(pair(4)) # retournera 1
    
    # ------------------------------------------

    # Example 3 
    # print(maximum(2, 5, 4)) # retournera 5
    ...