from lisibilite import lisibilite
from tri_formation import tri_formation,fusion
from candidature import candidature
from recuperation_des_donnes import recuperation_donnes
from tri_classement import tri_classement,fusionn
import random
# génére un dictionnaire pour faire les testes
def generer_random_liste():
    dico = []
    for i in range(10):
        candidate_id = random.randint(1, 10)
        program_id = random.randint(1, 3)
        score = random.randint(0, 500)
        timestamp = random.randint(0, 500)
        is_scholarship = random.randint(0, 1)
        hs_id = random.randint(0, 50)

        dico.append({
            "candidate_id": candidate_id,
            "program_id": program_id,
            "score": score,
            "timestamp": timestamp,
            "is_scholarship": is_scholarship,
            "hs_id":hs_id
        })
    
    return dico

dico = generer_random_liste()


# pour lisibilite.py

test1 = lisibilite(dico)

for i in test1 : 
    print(i)

print(" ")

#pour tri_formation.py

test2 = tri_formation(dico)
    
for i in test2:
    print(i)

print(" ")

#pour candidature.py

print(candidature(dico,1))
print (" ")

#pour recuperation_des_donnes

#print(recuperation_donnes("APP3_Fichiers-20260409/parcoursup_programs_small_800.csv"))
#print(" ")

#pour tri_classement.py
print("tri classement ")
print(tri_classement(dico))