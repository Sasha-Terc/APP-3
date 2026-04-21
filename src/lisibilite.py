#Code de benjamin

"""donne juste les valeurs car les clé sont les même
et ça a un rendu plus lisible"""

def lisibilite(liste_dicos):
    liste = []
    for dico in liste_dicos:
        liste.append(list(dico.values()))
    return liste




