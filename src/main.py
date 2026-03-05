

from distance_module import manhattan_manual, manhattan_scipy


def read_vectors_from_file(filename):
  
    with open(filename, 'r') as file:
        lines = file.readlines()

    v1 = list(map(float, lines[0].split()))
    v2 = list(map(float, lines[1].split()))

    return v1, v2


def main():
  
    filename = "input.txt"

    v1, v2 = read_vectors_from_file(filename)


    dist_manual = manhattan_manual(v1, v2)

  
    dist_scipy = manhattan_scipy(v1, v2)

    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("\nDistanța Manhattan (manual):", dist_manual)
    print("Distanța Manhattan (scipy):", dist_scipy)


if __name__ == "__main__":
    main()
