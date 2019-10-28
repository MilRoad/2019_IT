import matplotlib.pyplot as plt
import numpy as np
from math import pi


def if_pfront(id, X):
     for i, vec in enumerate(X):
         if i != id and np.all(X[id, :] <= vec):
             return False
     return True

def pareto_splits(X, N):
    pfront = []
    not_pfront = []
    for i in range(N):
        if if_pfront(i, X):
            pfront.append(X[i])
        else:
            not_pfront.append(X[i])
    return pfront, not_pfront


if __name__ == "__main__":
    N = 20
    M = 3
    X = np.random.rand(N, M) * 10

    pfront_vec, not_pfront_vec = pareto_splits(X, N)
    alpha = 2 * np.pi * np.arange(0, 1 + 1 / M, 1 / M)

    fig, axes = plt.subplots(ncols=1, subplot_kw=dict(polar=True))

    axes.set_title('Pareto front')
    for vec in pfront_vec:
        axes.plot(alpha, np.append(vec, vec[0]))

    plt.show()
