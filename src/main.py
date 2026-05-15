from candidature import candidature
from lisibilite import lisibilite
from recuperation_des_donnees import recuperation_donnees
from tri_classement import tri_classement
from tri_formation import tri_formation

# choix du fichier

fichier = input(""" 
Quel fichier voulez vous voir ? :
small      --> 1

medium     --> 2

massive    --> 3

(choisissez avec les chiffres correspondant sinon ça mettra le numéro 1 par défaut)
""")

chiffres = "123"

if fichier not in chiffres or fichier == "1" :
    fichier_programs = "APP3_Fichiers-20260409/parcoursup_programs_small_800.csv"
    fichier = "APP3_Fichiers-20260409/parcoursup_small_10000.csv"
    valeur_max = 800
else:
    if fichier == "2":
        fichier_programs = "APP3_Fichiers-20260409/parcoursup_programs_medium_2500.csv"
        fichier = "APP3_Fichiers-20260409/parcoursup_medium_100000.csv"
        valeur_max = 10000
    else:
        fichier_programs = "APP3_Fichiers-20260409/parcoursup_programs_massive_5000.csv"
        fichier = "APP3_Fichiers-20260409/parcoursup_massive_500000.csv"
        valeur_max = 2500

# récupération des données 
donnees = recuperation_donnees(fichier)
donnees_programs = recuperation_donnees(fichier_programs)

# met les données sous forme de liste, les clés dépendent du fichier choisi
print("Voici les données que vous avez choisi : ")
readable = lisibilite(donnees)

for i in readable:
    print(i)

print("Voici les données des programmes : ")
readable_programs = lisibilite(donnees_programs)
for i in readable_programs:
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

        print("Voici les données de la candidature {} : ".format(candidate_id))    
        print(candidature(donnees,candidate_id))
elif choix == "2":
    print("Voici les candidatures triées par formation : ")
    tri = tri_formation(donnees)
    for i in tri:
        print(i)  

    choix = input("""
Voulez vous trier les candidatures par classement ? :
oui  --> 1
non  --> 2
(choisissez avec les chiffres correspondant sinon ça mettra le numéro 2 par défaut)
""")
    if choix == "1":
        print("Voici les candidatures triées par classement : ")
        tri = tri_classement(donnees)
        tri = tri_formation(tri)
        for i in tri:
            print(i)
        choix = input("""
voulez vous voir la liste des candidats retenus par formation ? :
oui  --> 1
non  --> 2
(choisissez avec les chiffres correspondant sinon ça mettra le numéro 2 par défaut)
""")
        
