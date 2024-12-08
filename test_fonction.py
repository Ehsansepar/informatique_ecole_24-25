def int_input(message) :
    continuer = False
    while continuer == False:
        messages = input(message)
        if messages.isdigit() == True :
            messages = int(messages)
            continuer = True
            # return message
    return messages

def int_input1(message, minimum, maximum):
    while True:
        # Demander à l'utilisateur d'entrer un nombre
        reponse = input(message)
        
        # Vérifier si l'entrée contient uniquement des chiffres
        if reponse.isdigit():
            valeur = int(reponse)
            # Vérifier si le nombre est dans la plage demandée
            if minimum <= valeur <= maximum:
                return valeur
            else:
                print(f"Le nombre doit être compris entre {minimum} et {maximum}")
        else:
            print("Veuillez entrer un nombre entier valide")
            
    ...
    
def int_input3(message) :
    ...
if __name__ == "__main__" : 
    # nombre = int_input("Entrez un nombre : ")
    # print(f"{nombre} = {type(nombre)}")
    print(int_input1("Entrez un nombre : ", 1, 10))
    # print(f"{nombre} = {type(nombre)}")
