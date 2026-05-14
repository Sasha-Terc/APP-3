#code de antonin

#### pour les tests seulement
# mise en forme de la liste pour les tris
def liste_score(dico):
    Liste = []
    for d in dico:
            if d["score"] not in Liste:
                Liste.append(d["score"])
    return Liste
Liste = liste_score(dico)
print(Liste)
# verif de la liste
####


def tri_Classement(liste_dicos):
    if len(liste_dicos) < 2:
        return liste_dicos
    e = liste_dicos[0]
    L1, L2 = [], []
    for x in liste_dicos[1:]:
        if x > e:
            L1.append(x)
        else:
            L2.append(x)
    return tri_Classement(L1) + [e] + tri_Classement(L2)
#print(tri_Classement(liste_dicos))
