#Créer un programme job16.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini.
#La fonction écrira tous les paramètres dans le terminal.


def myFunction(*param):
        print(*param)

myFunction("1", "2", "3", "4", "5","Bravo ! On peux compter jusqu'a 5 !")