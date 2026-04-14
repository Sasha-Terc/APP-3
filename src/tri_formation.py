#code de sasha
def id_formations(dico):
    liste_forma = []
    for i in dico :
        if i[4] not in liste_forma :
            liste_forma.append(i[4])
        else : 
            continue
    return liste_forma
