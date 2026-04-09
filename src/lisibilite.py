#Code de benjamin
def lisibilite(dico):
    for i in dico:
        print(i)

def lisibilite_formation(dico,formation):
    L = []
    for i in dico:
        if i["program_id"] == formation:
            L.append[i]
    return L

