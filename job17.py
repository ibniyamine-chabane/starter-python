#Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
#- Remplir une liste myList contenant tous ces paramètres.
#- Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.

def myFunction(*params):
    myList= []
    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
    else:
        print("Attention un des paramètre n'est pas numérique")

    for element in myList:
        if element % 2 == 0:
            print(element)

myFunction(3,6,89,78,66,"jhjkg",2)
