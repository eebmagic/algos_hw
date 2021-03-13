import random
import time

def find_k_smallest(a, b, k):
    m = []
    i = 0
    j = 0
    while len(m) - 1 < k:
        # print(len(m)-1, k)
        if i >= len(a):
            m += b[j:]
        elif j >= len(b):
            m += a[i:]
        else:

            if a[i] <= b[j]:
                m.append(a[i])
                i += 1
            else:
                m.append(b[j])
                j += 1

    print(m)
    return m[k]


def kth(a, b, k, i=0, j=0):
    # return using the rest of opposing array once one
    # pointers reaches the end of its corresponding array
    if (i == len(a)):
        return b[j + k - 1]
    if (j == len(b)):
        return a[i + k - 1]
 
    # Return null if invalid inputs
    if (k == 0 or k > (len(a) - i) + (len(b) - j)):
        return -1

    # if k is 1 then return the kth value
    # (should be the smaller value at the two pointers)
    if (k == 1):
        if(a[i] < b[j]):
            return a[i]
        else:
            return b[j]
 
    # Select an array to to return from,
    # or increment its pointer and recurse
    if(k//2 - 1 >= len(a) - i):
        # if end of a is smaller than current point at b,
        # then return correct value from b
        if (a[-1] < b[j + k//2 - 1]):
            return b[j + (k - (len(a) - i) - 1)]
        else:
            return kth(a, b, k - k//2, i, j + k//2)
    if (k//2 - 1 >= len(b) - j):
        if (b[-1] < a[i + k//2 - 1]):
            return a[i + (k - (len(b) - j) - 1)]
        else:
            return kth(a, b, k - k//2, i + k//2, j)

    else:
        # if a at pointer is smaller, then for a
        # halve k, increment the pointer, and recruse
        if (a[k//2 + i - 1] < b[k//2 + j - 1]):
            return kth(a, b, k - k//2, i + k//2, j)
        
        # for b halve k, increment the pointer, and recruse
        else:
            return kth(a, b, k - k//2, i, j + k//2)


def test(minsize=10, maxsize=100, minval=0, maxval=100*2):
    A = random.randint(minsize, maxsize)
    B = random.randint(minsize, maxsize)
    a = [random.randint(minval, maxval) for x in range(A)]
    b = [random.randint(minval, maxval) for x in range(B)]

    a.sort()
    b.sort()

    k = random.randint(0, A+B-1)

    start = time.time()
    out = find_k_smallest(a, b, k)
    duration = time.time() - start

    return duration, (A, B, k), out


if __name__ == '__main__':
    a = [1, 5, 8]
    b = [2, 3, 7]
    k = random.randint(0, len(a) + len(b) - 1)
    both = a + b
    both.sort()

    # print(a)
    # print(b)
    # print(both)
    # print(k+1)

    out = kth(a, b, k+1)
    print(out, both[k], out == both[k])
    quit()

    # out = find_k_smallest(a, b, k)
    # print(f'output: {out}')

    x = []
    y = []
    iters = 100

    for _ in range(iters):
        duration, data, out = test(maxsize=10_000, maxval=10_000*2)
        total = data[0] + data[1]

        x.append(total)
        y.append(duration)

    import matplotlib.pyplot as plt
    plt.scatter(x, y)
    plt.show()