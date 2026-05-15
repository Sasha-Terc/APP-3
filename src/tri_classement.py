def fusionn(l1,l2): 
    liste = []
    i,j=0,0
    while i < len(l1) and j < len(l2):
        if l1[i]["score"] <= l2[j]["score"]:
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

def tri_classement(candidatures): 
    L1 , L2 = [], []
    if len(candidatures) < 2 :
        return candidatures[:2]
    else :
        mid =   len(candidatures) // 2
        l1 = tri_classement(candidatures[:mid])
        l2 = tri_classement(candidatures[mid:])
        return fusionn(l1,l2)

