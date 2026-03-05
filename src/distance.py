
from scipy.spatial.distance import cityblock


def manhattan_manual(v1, v2):
  
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie să aibă aceeași lungime!")

    distance = 0
    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i])

    return distance


def manhattan_scipy(v1, v2):
  
    return cityblock(v1, v2)
