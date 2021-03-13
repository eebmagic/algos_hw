import time
import random

def build_arr(n, minValue=0, maxValue=100):
    '''
    Build a random array of size n
    '''
    out = []
    for i in range(n):
        out.append(random.randint(minValue, maxValue))

    return out


def build_matr(inputArr):
    '''
    Build the square matrix from an input array
    Doing a sum for each position
    '''
    start = time.time()
    out = [[None] * len(inputArr)] * len(inputArr)
    for i in range(len(inputArr)):
        for j in range(len(inputArr)):
            if not i >= j:
                value = sum(inputArr[i:j])
                out[i][j] = value

    duration = time.time() - start
    return out, duration


def new_build_matr(inputArr):
    '''
    Based on my sudo code that that should be O(n^2)
    '''
    start = time.time()
    out = [[None] * len(inputArr)] * len(inputArr)

    for i in range(len(inputArr)):
        for j in range(i, len(inputArr)):
            if i == j:
                out[i][j] = inputArr[i]
            else:
                out[i][j] = out[i][j-1] + inputArr[j]

    duration = time.time() - start
    return out, duration


if __name__ == '__main__':
    from tqdm import tqdm
    start, stop = 1, 1000
    skip = 10

    x = []
    y = []
    # for i in tqdm(range(start, stop)):
    for i in range(start, stop, skip):
        arr = build_arr(i)
        # out, duration = build_matr(arr)
        out, duration = new_build_matr(arr)
        
        # points.append((i, duration))
        x.append(i)
        y.append(duration)
        print(f"{i}, {duration}")

    import matplotlib.pyplot as plt

    plt.scatter(x, y)
    plt.show()

