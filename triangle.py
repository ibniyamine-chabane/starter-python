#Écrire un programme triangle.py qui affiche dans le terminal un triangle avec des ‘_’, des
#‘\’ et des ‘/’
#en fonction de l’input entré, qui représentera la hauteur.
#Exemple si l’input entré est 5

left = "/"
right = "\\"
base = "__"

userinput = int(input("hauteur : "))


for i in range(userinput):
    print((userinput - i) * " " + left + ((i * 2) * ' ') + right)
    if i == userinput - 1:
        print(left + base * userinput + right)