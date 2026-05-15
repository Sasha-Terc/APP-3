from random import randint
from timeit import default_timer as timer
from tri_classement import tri_classement_fusion, tri_classement_rapide
from matplotlib import pyplot as plt

def bench(liste, func):
    t1 = timer()
    func(liste)
    t2 = timer()
    return t2 - t1

def generer_liste_aleatoire(n):
    return [randint(0, 100000) for _ in range(n)]

from random import randint
from timeit import default_timer as timer
from tri_classement import tri_classement_fusion, tri_classement_rapide
from matplotlib import pyplot as plt

def bench(liste, func):
    t1 = timer()
    func(liste)
    t2 = timer()
    return t2 - t1

def generer_liste_aleatoire(n):
    return [randint(0, 100000) for _ in range(n)]

from random import randint
from timeit import default_timer as timer
from tri_classement import tri_classement_fusion, tri_classement_rapide
from matplotlib import pyplot as plt

def bench(liste, func):
    t1 = timer()
    func(liste)
    t2 = timer()
    return t2 - t1

def generer_liste_aleatoire(n):
    return [randint(0, 100000) for _ in range(n)]

def tableau(sizes, func1, func2):
    temps_fusion = bench(func1, generer_liste_aleatoire())
    temps_rapide = bench(func2, generer_liste_aleatoire())  

    

    plt.plot(sizes, temps_fusion, marker="o", label="Tri fusion")
    plt.plot(sizes, temps_rapide, marker="s", label="Tri rapide")
    plt.xlabel("Taille de la liste", len(sizes))
    plt.ylabel("Temps d'exécution (secondes)")
    plt.title("Comparaison : Tri fusion vs Tri rapide")
    plt.legend()
    plt.grid(True)
    plt.show()