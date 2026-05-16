def fusionn(l1,l2): 
    liste = []
    i,j=0,0
    while i < len(l1) and j < len(l2):
        if int(l1[i]["score"]) <= int(l2[j]["score"]):
            liste.append(l1[i])
            i += 1
        else:
            liste.append(l2[j])
            j += 1
    while i < len(l1):
        liste.append(l1[i])
        i+=1
    while j < len(l2):
        liste.append(l2[j])
        j+=1
    return liste

def tri_classement_fusion(candidatures): 
    L3 , L4 = [], []
    if len(candidatures) < 2 :
        return candidatures
    else :
        mid =   len(candidatures) // 2
        L3 = candidatures[:mid]
        L4 = candidatures[mid:]
        l1 = tri_classement_fusion(L3)
        l2 = tri_classement_fusion(L4)
        return fusionn(l1,l2)

def tri_classement_rapide(candidatures):
    if len(candidatures) < 2:
        return candidatures[:2]
    pivot = candidatures[0]
    score_pivot = int(pivot["score"])
    L1,L2 = [],[]
    for x in candidatures[1:]:
        if int(x["score"]) < score_pivot:
            L1.append(x)
        else:
            L2.append(x)
    return tri_classement_rapide(L1) + [pivot] + tri_classement_rapide(L2)
