from lisibilite import lisibilite,lisibilite_formation
from random import randint,random



# verificateur pour lisibilité
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
test1 = lisibilite(dico)
test2 = [lisibilite_formation(dico,1),lisibilite_formation(dico,2),lisibilite_formation(dico,3)]

print(dico)
print(test1)
print(test2)