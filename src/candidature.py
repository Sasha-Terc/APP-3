# permet de retrouver les information d'un candidat


def candidature(dico,candidate_id):
    for i in dico:
        if i["candidate_id"] == candidate_id:
            return {"candidate_id": i["candidate_id"], "program_id": i["program_id"], "score": i["score"], "timestamp": i["timestamp"], "is_scholarship": i["is_scholarship"], "hs_id": i["hs_id"]}
        else:
            pass