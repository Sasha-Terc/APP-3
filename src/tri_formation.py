
def fusion(l1,l2): 
    liste = []
    i,j=0,0
    while i < len(l1) and j < len(l2):
        if l1[i][2] < l2[j][2]:
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
        return formations[:2]
    else :
        mid =   len(formations) // 2
        l1 = formations[:mid]
        l2 = formations[mid:]
        return fusion(l1,l2)



