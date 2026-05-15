from random import randint
from timeit import default_timer as timer
from tri_classement import tri_classement_fusion, tri_classement_rapide
from matplotlib import pyplot as plt

def bench(liste, func):
    t1 = timer()
    func(liste)
    t2 = timer()
    return t2 - t1

def tableau(liste):
    t1 = bench(liste, tri_classement_fusion(liste))
    t2 = bench(liste, tri_classement_rapide(liste))
    plt.plot([len(liste)], [t1], marker='o', label="Tri fusion")
    plt.plot([len(liste)], [t2], marker='s', label="Tri rapide")
    plt.xlabel("Taille de la liste (n)")
    plt.ylabel("Temps d'exécution (secondes)")
    plt.title("Comparaison : Tri fusion vs Tri rapide")
    plt.legend()
    plt.grid(True)
    plt.show()