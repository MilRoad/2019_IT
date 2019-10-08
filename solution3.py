import numpy as np


def get_indices(N, n_batches, split_ratio):
    i = 0
    k = ((N - 1) * (1 + split_ratio)) / (n_batches * split_ratio + 1)
    j = k / (1 + split_ratio)
    delta = k * (split_ratio / (1 + split_ratio))

    for l in range(n_batches):
        yield np.array([int(i), int(j), int(k)])
        i += delta
        j += delta
        k += delta

def main():
     for inds in get_indices(100, 5, 0.25):
         print(inds)
     # expected result:
     # [0, 44, 55]
     # [11, 55, 66]
     # [22, 66, 77]
     # [33, 77, 88]
     # [44, 88, 99]


if __name__ == "__main__":
     main()