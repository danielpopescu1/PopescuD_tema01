"""
distance_module.py

Acest modul conține funcții pentru calculul distanței Manhattan
între doi vectori:
1. Implementare manuală
2. Implementare folosind scipy
"""

from scipy.spatial.distance import cityblock


def manhattan_manual(v1, v2):
    """
    Calculează manual distanța Manhattan dintre doi vectori.

    Formula:
    d = Σ |v1[i] - v2[i]|

    :param v1: lista de numere (vector 1)
    :param v2: lista de numere (vector 2)
    :return: distanța Manhattan (float)
    """
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie să aibă aceeași lungime!")

    distance = 0
    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i])

    return distance


def manhattan_scipy(v1, v2):
    """
    Calculează distanța Manhattan folosind funcția
    cityblock() din scipy.

    :param v1: lista de numere (vector 1)
    :param v2: lista de numere (vector 2)
    :return: distanța Manhattan (float)
    """
    return cityblock(v1, v2)