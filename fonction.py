# --- Importation des modules python ---


# --- Définition des fonctions ---

# ex 1

def somme(liste) :
    total = 0 
    # i = 0
    # while i < len(liste) :
    #     total += liste[i]
    #     i += 1
    
    for nbr in range(len(liste)) :
        total += liste[nbr]
    return total

if __name__ == "__main__":
    # Example 1
    # l = [5, 8, 9, 47, 36, 123, 5, 3, 1]
    # somme(l) # retournera 237.
    
    # ------------------------------------------


    ...