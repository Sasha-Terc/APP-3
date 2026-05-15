from random import randint
from timeit import default_timer as timer
from tri_classement import tri_classement_fusion, tri_classement_rapide
from tri_formation import tri_formation_fusion, tri_formation_rapide
import matplotlib as plt

def bench(liste, func):
    t1 = timer()
    func(liste)
    t2 = timer()
    return t2-t1  # retournez le temps écoulé

def bench_all(liste):
    print("Tri fusion : ", bench(liste, tri_classement_fusion))
    print("Tri rapide : ", bench(liste, tri_classement_rapide))