def add(x, y):
    x = int(''.join(x), 2)
    y = int(''.join(y), 2)
    total = x + y
    string = f"{total:b}"

    return [char for char in string]


def multiply(n, m):
    print(f'multiplying: {n} by {m}')
    largest = max(len(n), len(m))
    if largest == 1:
        print(n, m)
        return int(n[0]) * int(m[0])

    midpoint = largest // 2
    n_l = n[:midpoint]
    n_r = n[midpoint:]
    m_l = m[:midpoint]
    m_r = m[midpoint:]

    p_1 = multiply(n_l, m_l)
    p_2 = multiply(n_r, m_r)
    p_3 = multiply(add(n_l, n_r), add(m_l, m_r))

    out = (p_1 * (2 ** largest)) \
        + ((p_3 - p_1 - p_2) * (2 ** (largest / 2))) \
        + p_2

    return out


if __name__ == '__main__':
    a = 7
    b = 5
    a = [char for char in f"{a:b}"]
    b = [char for char in f"{b:b}"]

    out = multiply(a, b)
    print(out)
