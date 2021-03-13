from script import maj
from statistics import stdev
import random
import time

def print_dict(d):
    keys = list(d.keys())
    keys.sort()
    for x in keys:
        print(f"{x}: {d[x]}")

def slow_max(arr):
    counts = {}
    for x in arr:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1

    out = max(counts, key=counts.get)
    thresh = len(arr) // 2 + 1

    if counts[out] >= thresh:
        return out
    else:
        return None


trackings = {}
devs = {}
for n in range(1, 10_000, 100):
    times = []
    values = set()
    iters = 10
    for _ in range(iters):
        # n = 100
        MIN, MAX = 0, 1
        thresh = (n // 2) + 1
        arr = [random.randint(MIN, MAX) for _ in range(n)]
        # correct = slow_max(arr)
        # print(f'Correct Answer: {correct}')

        start = time.time()
        out = maj(arr)
        duration = time.time() - start

        # print("\nCOMPARISON:")
        # print(out==correct, out, correct)
        # print(duration)

        times.append(duration)
        # values.add(out == correct)

    print("\nN:", n)
    # print(times)
    # print(values)
    avg = sum(times) / len(times)
    # print("Max:", max(times))
    # print("Min:", min(times))
    # print("Average:", avg)
    # print("stdev:", stdev(times))

    trackings[n] = avg
    devs[n] = stdev(times)

x = list(trackings.keys())
y = list(trackings.values())

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.plot(list(devs.keys()), list(devs.values()))
plt.show()