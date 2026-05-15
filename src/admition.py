def admition(dico1, dico2):
    """
    Cette fonction permet de faire une liste qui contient les candidats retenus pour chaque formation
    ainsi qu'une autre liste qui contient les candidats qui ne sont pas retenus pour chaque formation
    Le dico1 correspond au classement des candidats par formation
    Le dico2 correspond au nombre de places disponibles pour chaque formation
    """
    retenus = []
    non_retenus = []
    for capacity in dico2:
        program_id = capacity["program_id"]
        places = capacity["capacity"]
        for candidature in dico1:
            if candidature["program_id"] == program_id:
                if len(retenus) < int(places):
                    retenus.append(candidature)
                else:
                    non_retenus.append(candidature)
    return retenus, non_retenus
        