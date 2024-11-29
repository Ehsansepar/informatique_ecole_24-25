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
if __name__ == "__main__" : 
    
    print(stat_chiffres(-112233))
    ...