def int_input(message) :
    continuer = False
    while continuer == False:
        messages = input(message)
        if messages.isdigit() == True :
            messages = int(messages)
            continuer = True
            # return message
    return messages

def int_input1(message, minimum, maximum) :
    ...
    
def int_input3(message) :
    ...
if __name__ == "__main__" : 
    nombre = int_input("Entrez un nombre : ")
    print(f"{nombre} = {type(nombre)}")