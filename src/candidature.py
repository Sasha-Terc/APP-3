# permet de retrouver les information d'un candidat


def candidature(dico,candidate_id):
    for i in dico:
        if i["candidate_id"] == candidate_id:
            return i
        else:
            pass