from random import randint
from timeit import default_timer as timer
from tri_classement import tri_classement_fusion, tri_classement_rapide
from tri_formation import tri_formation, tri_formation_rapide, tri_formation

def bench(liste, func):
    t1 = timer()
    func(liste)
    t2 = timer()
    return t2 - t1