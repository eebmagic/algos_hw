import numpy as np

def count_paths(v, n, a):
    # v: number of vertices, n: expected path length
    paths = 0    
    b = np.array(a, copy=True)

    for i in range(n-2):
        b = np.dot(b, a)

    c = np.dot(b, a)
    x = c - b

    print(x)

    for i in range(v):
        for j in range(i+1, v):
            if x[i][j] == 1:
                paths = paths + 1

    return paths

x = count_paths(5, 2, np.array([
                np.array([0, 1, 0, 0, 0]),
                np.array([1, 0, 1, 0, 1]),
                np.array([0, 1, 0, 1, 0]),
                np.array([0, 0, 1, 0, 0]),
                np.array([0, 1, 0, 0, 0])
            ]))

print(x)