#from candidat import candidat
from lisibilite import lisibilite
from recuperation_des_donnes import recuperation_donnes
#from tri_classement import tri_Classement
from tri_formation import tri_formation

# choix du fichier

fichier = input(""" 
Quel fichier voulez vous voir ? :
parcoursup_programs_small_800       --> 1

parcoursup_programs_small_10000     --> 2

parcoursup_programs_medium_2500     --> 3

parcoursup_programs_medium_100000   --> 4

parcoursup_programs_massive_5000    --> 5

parcoursup_programs_massive_500000  --> 6

(choisissez avec les chiffres correspondant sinon ça mettra le numéro 1 par défaut)
""")

chiffres = ["1","2","3","4","5","6"]

if fichier not in chiffres or fichier == "1" :
    fichier = "APP3_Fichiers-20260409/parcoursup_programs_small_800.csv"
else:
    if fichier == "2":
        fichier = "APP3_Fichiers-20260409/parcoursup_small_10000.csv"
    elif fichier == "3":
        fichier = "APP3_Fichiers-20260409/parcoursup_programs_medium_2500.csv"
    elif fichier == "4":
        fichier = "APP3_Fichiers-20260409/parcoursup_medium_100000.csv"
    elif fichier == "5":
        fichier = "APP3_Fichiers-20260409/parcoursup_programs_massive_5000.csv"
    else:
        fichier = "APP3_Fichiers-20260409/parcoursup_massive_500000.csv"

# récupération des données 
donnes = recuperation_donnes(fichier)

# met les données sous forme de liste, les clés dépendent du fichier choisi
readable = lisibilite(donnes)

for i in readable:
    print(i)

