from random import randint
from timeit import default_timer as timer
from tri_classement import tri_classement_fusion, tri_classement_rapide
from matplotlib import pyplot as plt

def bench(liste, func):
    t1 = timer()
    func(liste)
    t2 = timer()
    return t2 - t1