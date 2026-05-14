from candidature import candidature
from lisibilite import lisibilite
from recuperation_des_donnees import recuperation_donnees
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
    valeur_max = 800
else:
    if fichier == "2":
        fichier = "APP3_Fichiers-20260409/parcoursup_small_10000.csv"
        valeur_max = 10000
    elif fichier == "3":
        fichier = "APP3_Fichiers-20260409/parcoursup_programs_medium_2500.csv"
        valeur_max = 2500
    elif fichier == "4":
        fichier = "APP3_Fichiers-20260409/parcoursup_medium_100000.csv"
        valeur_max = 100000
    elif fichier == "5":
        fichier = "APP3_Fichiers-20260409/parcoursup_programs_massive_5000.csv"
        valeur_max = 5000
    else:
        fichier = "APP3_Fichiers-20260409/parcoursup_massive_500000.csv"
        valeur_max = 500000

# récupération des données 
donnees = recuperation_donnees(fichier)

# met les données sous forme de liste, les clés dépendent du fichier choisi
readable = lisibilite(donnees)

for i in readable:
    print(i)

# maintenant qu'on a les donnees, on choisi ce qu'on veut faire
choix = input("""
Que voulez vous faire ? :
chercher les donnees d'une candidature  --> 1
trier les candidature par formation     --> 2
comparer les tri implementes            --> 3

(choisissez avec les chiffres correspondant sinon ça mettra le numéro 1 par défaut)
""")

chiffres = ["1","2","3"]
# on cherche les donnees d'un candidat 
if valeur_max == 10000 or valeur_max == 100000 or valeur_max == 500000 :
    if choix not in chiffres or choix == "1" :
        chaine = ""
        candidate_id = input("""
quels est l'id du candidat ?
( répondez avec un nombre de 0 à {})
""".format(valeur_max))
        for i in range (valeur_max + 1):
            chaine += str(i) + ","

        while candidate_id not in chaine :
            print("ce candidat n'existe pas")
            candidate_id = input("""
quels est l'id du candidat ?
( répondez avec un nombre de 0 à {})
""".format(valeur_max))
    

        print(candidature(donnees,candidate_id))
