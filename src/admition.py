def admition(dico1, dico2):
    """
    Cette fonction permet de faire une liste qui contient les candidats retenus pour chaque formation
    ainsi qu'une autre liste qui contient les candidats qui ne sont pas retenus pour chaque formation
    Le dico1 correspond au classement des candidats par formation (déjà trié)
    Le dico2 correspond au nombre de places disponibles pour chaque formation
    """
    retenus = []
    non_retenus = []
    
    # Index pour parcourir dico1 sans repasser sur les candidats déjà traités
    i = 0
    n = len(dico1)
    
    for capacity in dico2:
        program_id = capacity["program_id"]
        places = int(capacity["capacity"])
        compteur = 0
        
        # On avance dans dico1 tant qu'on est sur la bonne formation
        while i < n and dico1[i]["program_id"] == program_id:
            if compteur < places:
                retenus.append(dico1[i])
                compteur += 1
            else:
                non_retenus.append(dico1[i])
            i += 1
    
    return retenus, non_retenus