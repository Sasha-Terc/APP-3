def recuperation_donnes(fichier):

    with open(fichier, "r", encoding="utf-8") as fichier_ouvert:
        lignes = []
        for ligne in fichier_ouvert:
            ligne_nettoyee = ligne.strip()
            if ligne_nettoyee:
                lignes.append(ligne_nettoyee)

    if not lignes:
        return []

    premiere_ligne = lignes[0]
    separateur = ";"
    if "," in premiere_ligne:
        separateur = ","
    
    entetes = []
    for morceau in premiere_ligne.split(separateur):
        entetes.append(morceau.strip())

    resultats = []
    for ligne in lignes[1:]:
        valeurs = []
        for valeur in ligne.split(separateur):
            valeurs.append(valeur.strip())

        dictionnaire = {}
        for index, cle in enumerate(entetes):
            if index < len(valeurs):
                dictionnaire[cle] = valeurs[index]
            else:
                dictionnaire[cle] = ""
        resultats.append(dictionnaire)

    return resultats
