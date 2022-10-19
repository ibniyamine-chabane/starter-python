#Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et qui
#compte le nombre de noms de domaine.


#------------------Mon Code----------------------------------
f = open("domains.xml", "r")

list = []
lignes = f.readlines()
for line in lignes:
    line = line.replace("</column>\n", "")
    list.append(line)
f.close()
list2 = [s for s in list if '<column name="domain">' in s]
print(len(list2))

#------------------Correction-------------------

#from xml.dom import minidom
#
#doc = minidom.parse('domains.xml')
#elements = doc.getElementsByTagName("column")
#newList = []
#
#for element in elements:
#    if element.getAttribute("name") == "domain":
#        newList.append(element.childNodes[0].data)
#
#print(len(newList))