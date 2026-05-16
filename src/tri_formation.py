
def fusion(l1,l2): 
    liste = []
    i,j=0,0
    while i < len(l1) and j < len(l2):
        if int(l1[i]["program_id"]) < int(l2[j]["program_id"]):
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

def tri_formation(formations): 
    if len(formations) < 2 :
        return formations[:]
    else :
        mid =   len(formations) // 2
        l1 = tri_formation(formations[:mid])
        l2 = tri_formation(formations[mid:])
    return fusion(l1,l2)

def tri_formation_rapide(formations):
    if len(formations) < 2:
        return formations[:]
    pivot = formations[0]
    program_id_pivot = int(pivot["program_id"])
    L1,L2 = [],[]
    for x in formations[1:]:
        if int(x["program_id"]) < program_id_pivot:
            L1.append(x)
        else:
            L2.append(x)
    return tri_formation_rapide(L1) + [pivot] + tri_formation_rapide(L2)


