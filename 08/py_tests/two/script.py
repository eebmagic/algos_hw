import math

def a(weights, r=1):
    return sum(weights) * r

def b(weights, c=10):
    return c * math.ceil(len(weights) / 4) * 4


def solve(weights, r, c):
    OPT = {0:0}
    out = ""
    for i, w in enumerate(weights):
        i = i + 1
        a, b = float('inf'), float('inf')
        if i-1 in OPT:
            a = (r*w) + OPT[i-1]

        if i-4 in OPT:
            b = (c*4) + OPT[i-4]

        m = min(a, b)
        OPT[i] = m
        selection = "ab"[[a, b].index(m)]
        out += selection

    return out, m


if __name__ == '__main__':
    weights = [11,9,9,12,12,12,12,9,9,11]

    out = solve(weights, r=1, c=10)
    print(out)
