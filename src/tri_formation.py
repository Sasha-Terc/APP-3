#code de sasha
"""désolé j'avais fait ça en cours 
suite a une demande que tu m'as fait 
mais au final ça tri tout par formation """


def tri_formation(dico,formation):
    L = []
    for i in dico:
        if i["program_id"] == formation:
            L.append([i])
    return L