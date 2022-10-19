#Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
#le nombre de mots (sans caractère spéciaux) qui s’y trouvent.


#-------------------Mon Code (qui ne marche pas T-T------------)
f = open("data.txt", "r")

list = []
lignes = f.readlines()
for line in lignes:
    list.append(line)
#f.close()
list2 = [s for s in list if '+' in s]
print(len(list2))

#---------------Correction----------------

#import re 
#
#fichier = open("data.txt","r")
#text = fichier.read()
#pattern = '[a-zA-Z]+'
#matches = re.findall(pattern, text)
#
#print(len(matches))