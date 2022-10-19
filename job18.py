#Créer un programme job18.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
#- Remplir une liste myList contenant tous ces paramètres.
#- Trier par ordre croissant la liste à l’aide de la fonction sort
#- Afficher la liste dans un terminal


def myFunction(*params):
    myList= []
    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
    else:
        print("Attention un des paramètre n'est pas numérique")

    print(myList)

myFunction(3,6,89,78,66,"jhjkg",2)