from candidature import candidature
from lisibilite import lisibilite
from recuperation_des_donnees import recuperation_donnees
from tri_classement import tri_classement_fusion, tri_classement_rapide
from tri_formation import tri_formation
from admition import admition
from tableau import bench

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
    valeur_max = 10000
    valeur_max_programs = 800
else:
    if fichier == "2":
        fichier_programs = "APP3_Fichiers-20260409/parcoursup_programs_medium_2500.csv"
        fichier = "APP3_Fichiers-20260409/parcoursup_medium_100000.csv"
        valeur_max = 100000
        valeur_max_programs = 2500
    else:
        fichier_programs = "APP3_Fichiers-20260409/parcoursup_programs_massive_5000.csv"
        fichier = "APP3_Fichiers-20260409/parcoursup_massive_500000.csv"
        valeur_max = 500000
        valeur_max_programs = 5000

# récupération des données 
donnees = recuperation_donnees(fichier)
donnees_programs = recuperation_donnees(fichier_programs)

# pour evité des bugs pour la suite, on tri donnees_programs par program_id
donnees_programs = tri_formation(donnees_programs)
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
    chaine = []
    candidate_id = input("""
quels est l'id du candidat ?
( répondez avec un nombre de 1 à {})
""".format(valeur_max))
    for i in range (1,valeur_max + 1):
        chaine.append(str(i))

    while candidate_id not in chaine:
        print("ce candidat n'existe pas")
        candidate_id = input("""
quels est l'id du candidat ?
( répondez avec un nombre de 1 à {})
""".format(valeur_max))

        print("Voici les données de la candidature {} : ".format(candidate_id))    
        print(candidature(donnees,candidate_id))
elif choix == "2":
    chaine = ""
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
        tri = tri_classement_fusion(donnees)
        tri = tri_formation(tri)
        for i in tri:
            print(i)
        choix = input("""
voulez vous voir la liste des candidats retenus par formation ? :
oui  --> 1
non  --> 2
(choisissez avec les chiffres correspondant sinon ça mettra le numéro 2 par défaut)
""")
        if choix == "1":
            print("Voici la liste des candidats retenus par formation : ")
            retenus, non_retenus = admition(tri, donnees_programs)
            for i in retenus:
                print(i)
            choix = input("""
voulez vous une formation en particulier ? :
oui  --> 1
non  --> 2
(choisissez avec les chiffres correspondant sinon ça mettra le numéro 2 par défaut)""")
            if choix == "1":
                program_id = input("""
quels est l'id de la formation ?
( répondez avec un nombre de 1 à {})""".format(valeur_max_programs))
                
                chaine = ""
                for i in range (valeur_max_programs + 1):
                    chaine += str(i) + ","
                while program_id not in chaine or program_id == "0":
                    print("cette formation n'existe pas")
                    program_id = input("""
quels est l'id de la formation ?
( répondez avec un nombre de 0 à {})""".format(valeur_max_programs))
                print("Voici la liste des candidats retenus pour la formation {} : ".format(program_id))
                trouves = False
                for i in retenus:
                    if int(i["program_id"]) == int(program_id):
                        print(i)
                        trouves = True
                if not trouves:
                    print("Il n'y a pas de candidats retenus pour cette formation")
            else:
                choix = input("""
voulez vous voir la liste des candidats non retenus par formation ? :
oui  --> 1
non  --> 2
(choisissez avec les chiffres correspondant sinon ça mettra le numéro 2 par défaut)""")
                if choix == "1":
                    print("Voici la liste des candidats non retenus par formation : ")
                    for i in non_retenus:
                        print(i)
                    choix = input("""
voulez vous une formation en particulier ? :
oui  --> 1
non  --> 2
(choisissez avec les chiffres correspondant sinon ça mettra le numéro 2 par défaut)""")
                    if choix == "1":
                        program_id = input("""
quels est l'id de la formation ?
( répondez avec un nombre de 0 à {})""".format(valeur_max_programs))
                        chaine = ""
                        for i in range (valeur_max_programs + 1):
                            chaine += str(i) + ","

                        while program_id not in chaine or program_id == "0":
                            print("cette formation n'existe pas")
                            program_id = input("""
quels est l'id de la formation ?
( répondez avec un nombre de 0 à {})""".format(valeur_max_programs))
                        print("Voici la liste des candidats non retenus pour la formation {} : ".format(program_id))
                        trouves = False
                        for i in non_retenus:
                            if int(i["program_id"]) == int(program_id):
                                print(i)
                                trouves = True
                        if not trouves:
                            print("Il n'y a pas de candidats non retenus pour cette formation")
else :
    t1 = bench(donnees,tri_classement_fusion(donnees))
    t2 = bench(donnees,tri_classement_rapide(donnees))
    print("Voici le temps d'execution du tri fusion : ", t1)
    print("Voici le temps d'execution du tri rapide : ", t2)