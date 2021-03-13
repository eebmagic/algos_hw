import matplotlib.pyplot as plt
from math import log

def a(n):
    print(f'calling a with {n = }')
    if n <= 1:
        out = 0
    else:
        out = 49 * a(n // 25) + ((n ** (3/2))  * log(n))

    print(f'returning: a({n}) => {out}')
    return out


def b(n, c=2):
    if n <= 0:
        return c ** n
    return b(n-1) + (c ** n)

def c(n):
    if n <= 0:
        return 1

    return 2 * c(n - 1) + 1

def n_square(n):
    return n ** 2


def bounded(data, lower, upper, start=0):
    for i in range(len(data)):
        if i >= start:
            if lower[i] < data[i] and data[i] < upper[i]:
                pass
            else:
                print(f'False at {i}')
                print(f'{lower[i] = }')
                print(f'{data[i] = }')
                print(f'{upper[i] = }')
                return False
    return True

if __name__ == "__main__":
    # print(a(625))

    x = list(range(1, 625+1))
    # x = list(range(1, 25+1))
    y = [b(i) for i in x]
    y_2 = [2**n for n in x]
    y_3 = [2 * i for i in y_2]

    ## Correct examples for b
    # c = 2
    # x = list(range(1, 100))
    # y = [b(i, c=c) for i in x]
    # y_2 = [c ** n for n in x]
    # y_3 = [i*(c+1) for i in y_2]

    ## Correct examples for c
    # x = list(range(1, 10))
    # y = [c(i) for i in x]
    # y_2 = [2**n for n in x]
    # y_3 = [5 * i for i in y_2]

    back = 1
    print(x[-back:])
    print(y[-back:])
    print(y_2[-back:])
    print(y_3[-back:])
    print("")
    print(bounded(y, y_2, y_3))

    plt.plot(x, y, label='data')
    plt.plot(x, y_2, label='2^n')
    plt.plot(x, y_3, label='scaled 2^n')
    plt.legend()
    plt.show()