import numpy as np

from linear import Linear


def main():
    n = 1000
    d = 128
    x = np.random.random((n, d))
    query = np.random.random(d)

    linear = Linear()
    linear.add(x)
    indices, distances = linear.search(query)
    print(indices)
    print(distances)
    print("DONE")


if __name__ == "__main__":
    main()
