# Ehsan Separ 5TB Gr1

# --- Importation des modules python ---



# --- Définition des fonctions ---
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
    continuer = False
    
    while continuer == False:
        messages = input(message)
        
        if messages.isdigit():
            valeur = int(messages)
    
            if minimum <= valeur <= maximum:
                continuer = True
                return valeur
            else:
                print(f"Le nombre doit être compris entre {minimum} et {maximum}")
    
        else:
            print("Veuillez entrer un nombre entier valide")
            
    ...
    
def int_input3(message, minimum=None, maximum=None):
    nombre = ""
    
    while not nombre.isdigit():

        nombre = input(message)
        
        if not nombre.isdigit(): 
            print("Veuillez entrer un nombre valide.")
    
    valeur = int(nombre)  

    if minimum is not None and maximum is not None:
        if minimum <= valeur <= maximum:
            return valeur
        else:
            print(f"Le nombre doit être compris entre {minimum} et {maximum}")
            return int_input3(message, minimum, maximum) 

    elif minimum is not None:
        if valeur >= minimum:
            return valeur
        else:
            print(f"Le nombre doit être supérieur ou égal à {minimum}")
            return int_input3(message, minimum, maximum) 

    elif maximum is not None:
        if valeur <= maximum:
            return valeur
        else:
            print(f"Le nombre doit être inférieur ou égal à {maximum}")
            return int_input3(message, minimum, maximum)  

    return valeur 

        


def input_float() :
    nombre = ""
    while not nombre.isdigit():
        nombre = input("Entrez un nombre : ")
        if not nombre.isdigit():
            print("Veuillez entrer un nombre valide.")
    return float(nombre)

def input_yesno(message, default=True) :
    yn = ""
    while yn not in ['y', 'Y', 'o', 'O', 'N', 'n', '0', '0']:
        yn = input(message)
        if yn in ['y', 'Y', 'o', 'O']:
            return True
        elif yn in ['N', 'n', '0']:
            return False
        else:
            print("Veuillez entrer un choix valide.")
    # message + [y/N] : default == False
    # message + [Y/n] : default == True
    # ['y', 'Y', 'o', 'O', ]
    # ['N', 'n', '0', '0']
    return default

    ...

if __name__ == "__main__" :

    nombre = input_int("Entrez un nombre: ")
    print(f"{nombre = }, {type(nombre) = }")
    # Entrez un nombre entier quelconque
    nombre = input_float("Entrez un nombre: ")
    print(f"{nombre = }, {type(nombre) = }")
    # Entrez un nombre entier plus grand ou égal à 1
    nombre = input_int3("Entrez un nombre: ", 1)
    print(f"{nombre = }, {type(nombre) = }")
    # Entrez un nombre entier compris entre 1 et 20 inclus
    nombre = input_int1("Entrez un nombre: ", 1, 20)
    print(f"{nombre = }, {type(nombre) = }")
    # Entrez un nombre entier plus petit ou égal à 20
    nombre = input_int3("Entrez un nombre: ", None, 20)
    print(f"{nombre = }, {type(nombre) = }")
    nombre = input("Entrtez un nombre: ")
    nombre = int(nombre)
    ...
    