import matplotlib.pyplot as plt

def g(n, c):
    out = 1
    for i in range(1, n+1):
        out += c ** i
    return out



if __name__ == '__main__':
    # x = 10
    # c = 2
    # print(x, g(x, c))

    '''
    for theta(c ** n) if c > 1

    With c > 1, the geometric series will be c ^ n in addition to
    the values of n {0, n}. Therefore, y=c^n will always be a
    lower bound for g(n). A multiple of y=c^n will always be an
    upper bound for g(n) (not totally sure how to prove tho?).
    '''
    # x = []
    # y = []
    # ref = []
    # upper = []
    # c = 3
    # # stop = 100
    # stop = 10
    # for n in range(stop):
    #     x.append(n)
    #     y.append(g(n, c))
    #     ref.append(c ** n)
    #     upper.append(ref[-1] * 3)

    # for i in range(len(y)):
    #     print(i, y[i], ref[i], upper[i])
    #     print(f'n={i},', f'2**n = {2 ** i},', f'sum(0, {i}): {sum(list(range(0, i+1)))},', f'out: {y[i]}')
    #     print(i, 2 ** i, sum(list(range(0, i+1))), y[i])
    #     print('')

    # plt.plot(x, y)
    # plt.plot(x, ref)
    # plt.plot(x, upper)


    '''
    for theta(n) if c = 1

    With c = 1, the geometric series g(n) will always return n + 1,
    at this point y=n and y=3n will be upper and lower bounds.
    '''
    x = []
    y = []
    ref = []
    upper = []
    c = 1
    stop = 100
    for n in range(stop):
        x.append(n)
        y.append(g(n, c))
        ref.append(n)
        upper.append(n * 2)

    for i in range(len(y)):
        print(i, y[i], ref[i])

    plt.plot(x, y)
    plt.plot(x, ref)
    plt.plot(x, upper)

    '''
    for theta(1) if c < 1

    With c < 1 approaches a hard limit, at which point
    the constant 1 (or c_2 * 1) will be upper and lower bounds.
    '''
    # x = []
    # y = []
    # ref = []
    # upper = []
    # c = 1/2
    # stop = 100
    # for n in range(stop):
    #     x.append(n)
    #     y.append(g(n, c))
    #     ref.append(1)
    #     upper.append(ref[-1] * 3)

    # plt.plot(x, y)
    # print(max(y))
    # plt.plot(x, ref)
    # plt.plot(x, upper)

    plt.show()