
#Créer un programme job13.py qui demande à l’utilisateur de renseigner un nombre
#entier. Le programme devra alors parcourir le contenu du fichier “data.txt” compter le
#nombre de mots de la taille renseignée qui s’y trouvent.

# fait avec la correction

nbre = int(input("Entrer un nombre entier : "))

with open("data.txt", "r") as fichier:
    lines = fichier.read()

liste = lines.split()

nb_words = 0

for element in liste:
    if len(element) == nbre:
        nb_words = nb_words + 1

print(nb_words)