
def fusion(l1,l2): 
    liste = []
    i,j=0,0
    while i < len(l1) and j < len(l2):
        if l1[i]["program_id"] < l2[j]["program_id"]:
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

def tri_formation_fusion(formations): 
    if len(formations) < 2 :
        return formations[:2]
    else :
        mid =   len(formations) // 2
        l1 = formations[:mid]
        l2 = formations[mid:]
        L6 = tri_formation_fusion(l1)
        L7 = tri_formation_fusion(l2)
    return fusion(L6,L7)

def tri_formation_rapide(formations):
    if len(formations) < 2:
        return formations[:2]
    pivot = formations[0]
    program_id_pivot = pivot["program_id"]
    L1,L2 = [],[]
    for x in formations[1:]:
        if x["program_id"] < program_id_pivot:
            L1.append(x)
        else:
            L2.append(x)
    return tri_formation_rapide(L1) + [pivot] + tri_formation_rapide(L2)


