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

# Exercice 4

def indexMax(serie):
    maxi = 0
    index = 0
    for i in range(len(serie)) : 
        print(f"{i} {serie[i]}")
        if serie[i] > maxi :
            maxi = serie[i]
            index = i 
    return index

# -----------------------------------------------------------------------------

# exercice 5

def nomMois(n) : 
    mois = [
    "Janvier", 
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Août",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre"
]
    if 1 <= n <= 12 :
        return mois[(n-1)]
    else : 
        return None

# -----------------------------------------------------------------------------

# exercice 6 

def inverse(chaine) : 
    chaine = chaine[::-1]    
    return chaine

# -----------------------------------------------------------------------------

# exercice 7 

def compteMots(phrase):
    compteur = 0 
    mots = phrase.split()
    for mot in mots :
        compteur += 1
    return compteur

# -----------------------------------------------------------------------------

# exercice 8 

def occurrence(chaine, car) : 
    compteur = 0
    for i in range(len(chaine)) : 
        if chaine[i] == car :
            compteur += 1
    return compteur

# -----------------------------------------------------------------------------

# exercice 9

def str2list(chaine) : 
    new_lst = []
    for i in range(len(chaine)) :
        new_lst.append(chaine[i])
    return new_lst

# -----------------------------------------------------------------------------

# exercice 10

def find_num(matrix, nbre) : 
    compteur = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == nbre : 
                return (i, j)

# -----------------------------------------------------------------------------

# exercice 11 

def grands_mots(liste, nbre) : 
    new_lst = []
    for i in range(len(liste)) :
        if len(liste[i]) > nbre :
            new_lst.append(liste[i])

    if new_lst == [] : 
        return None
    return new_lst

# -----------------------------------------------------------------------------

# exercice 12 

def liste_paire(liste) :
    new_lst_pair = [] 
    for i in range(len(liste)) : 
        if i % 2 == 1 :
            new_lst_pair.append(liste[i] * 2)
        elif i % 2 == 0 :
            new_lst_pair.append(liste[i] // 2)
    return new_lst_pair

# -----------------------------------------------------------------------------

# exercice 13 

def occ_liste(liste, car) : 
    new_lst = []
    for i in range(len(liste)) :
        compteur = 0 
        for j in range(len(liste[i])) :
            if liste[i][j] == car :
                compteur += 1
        new_lst.append(compteur)
    return new_lst

# -----------------------------------------------------------------------------

#  Exercice 14

def stat_chiffres(nbre) : 
    nbr_str = str(abs(nbre))
    dictionaire = {}

    for chifre in nbr_str :
        if chifre in dictionaire :
            dictionaire[chifre] += 1
        else :
            dictionaire[chifre] = 1
    
    return dictionaire

# -----------------------------------------------------------------------------

# Exercice 15 



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

    # ------------------------------------------

    # Example 4 
    # serie = [5, 8, 2, 1, 9, 3, 6, 7]
    # print(indexMax(serie)) # retournera 4

    # ------------------------------------------

    # Example 5
    # print(nomMois(4)) # retournera "Avril"

    # ------------------------------------------

    # Example 6
    # print(inverse("hello"))

    # ------------------------------------------

    # Example 7
    # print(compteMots('bonjour à tous, je suis étudiant.'))

    # ------------------------------------------

    # Example 8
    # print(occurrence("une belle vache", "e")) # retournera 4

    # ------------------------------------------

    # Example 9 
    # print(str2list("hello !")) # retournera ["h","e","l","l","o"," ","!"].

    # ------------------------------------------

    # Example 10 
    # matrix = [[15, 23, 45],
    #           [39, 63, 78],
    #           [56, 45, 12]]
    # print(find_num(matrix, 45)) # retournera (0, 2)
    # print(find_num(matrix, 17)) # retournera None
    
    # ------------------------------------------

    # Example 11
    # l = ['crotale', 'python', 'boa', 'couleuvre', 'cobra']
    # print(grands_mots(l, 5)) # retournera ['crotale', 'python', 'couleuvre']
    # print(grands_mots(l, 9)) # retournera None.

    # ------------------------------------------

    # Example 12
    # serie = [4, 52, 13, 9, 16, 49, 756, 7]
    # print(liste_paire(serie)) # retournera [2, 104, 6, 18, 8, 98, 378, 14]

    # ------------------------------------------

    # Example 13 
    # ptit_dej = ['biscottes', 'chocolat', 'cafe', 'tartines', 'the']
    # print(occ_liste(ptit_dej, 'c')) # retournera [1, 2, 1, 0, 0]

    # ------------------------------------------

    # Example 14 
    # nbre = 452475
    # print(stat_chiffres(nbre)) # retournera {4: 2, 5: 2, 2: 1, 7: 1}
    # nbre = 11122544456666
    # print(stat_chiffres(nbre)) # retournera {1: 3, 2: 2, 5: 2, 4: 3, 6: 4}
    
    # ------------------------------------------
    
    # Example 15
    ...