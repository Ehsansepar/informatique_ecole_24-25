# 14

def stat_chiffres(nbre) : 
    nbr_str = str(abs(nbre))
    dictionaire = {}

    for chifre in nbr_str :
        if chifre in dictionaire :
            dictionaire[chifre] += 1
        else :
            dictionaire[chifre] = 1
    
    return dictionaire

def dictionnaire(nbr) : 
    nbr_to_str = str(nbr)
    dictionnaire_nbr = {}

    for i in nbr_to_str : 
        dictionnaire_nbr[i] 
    return dictionnaire_nbr
if __name__ == "__main__" : 
    
    print(stat_chiffres(-112233))
    print(dictionnaire(150))
    ...