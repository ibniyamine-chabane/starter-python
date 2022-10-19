#Écrire un programme job10.py qui demande à l’utilisateur d’entrer un texte. Le
#programme devra récupérer ce texte, et l’écrire dans un fichier “output.txt”.
#Écrire un programme qui lit le contenu de fichier “output.txt”, et qui l’écrit dans le
#terminal.


texte = input("texte : ")

fichier = open('output.txt', "w")
fichier.write(texte)
fichier.close

fichier = open('output.txt', "r")
print(fichier.read())
fichier.close

