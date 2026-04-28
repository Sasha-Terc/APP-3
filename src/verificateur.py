import lisibilite
from candidature import candidature
import random
from tri_formation import fusion,tri_formations
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

u = generer_random_liste()


# pour lisibilite.py

#test1 = lisibilite.lisibilite(dico)

#for i in test1 : 
    #print(i)

#print(" ")
#pour tri_formation.py
print(tri_formations(liste))


#pour candidature.py

#print(candidature(dico,1))
#print (" ")

#print(tri_formation(dico))