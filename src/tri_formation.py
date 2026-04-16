#code de sasha
def recup_formations(file) :  #fonction qui recupere les identifiants de formation dans un fichier et les stocke dans une liste
    formations = []
    with open(file, 'r') as f:
        u = f.readlines()
        for i in u:
            formations.append(i.strip())
    return formations

def slice_formation(formations): #fonction qui divise la liste des formations en deux parties
    if len(formations) < 2 :
        return formations[:2]
    else :
        mid =   len(formations) // 2
        l1 = formations[:mid]
        l2 = formations[mid:]
        return l1,l2

def tri_formation(l1,l2): #tri fusion en ordre croissant des identifiants de formation 
    liste = []
    i,i=0 
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
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

print(recup_formations(parcoursup_programs_small_800.csv))
