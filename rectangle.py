#Écrire un programme rectangle.py qui attend deux inputs : la largeur puis la hauteur.
#Votre programme devra ensuite dessiner un rectangle avec les éléments suivants :
#- des “|” pour dessiner les côtés droite et gauche
#- des “-” pour dessiner le haut et le bas
#- des espaces pour remplir le rectangle

hauteur = int(input("hauteur : "))
largeur = int(input("largeur : "))

side = "|"
separator = "-"

for i in range (hauteur):
    if i == 0 or i == hauteur -1:
        separator = "-"
    else:
        separator = " "
    print(side + separator * largeur + side)
