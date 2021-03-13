import matplotlib.pyplot as plt

class Line:
    # y = mx + b
    def __init__(self, m, b, name='line'):
        self.m = m
        self.b = b
        self.name = name

    def f(self, x):
        return (self.m * x) + self.b


def solution(a, b):
    '''
    find solution of two lines
    '''
    try:
        slopes = a.m - b.m
        offsets = b.b - a.b
        x = offsets / slopes
        y = a.f(x)
        return (x, y)
    except AttributeError:
        print(type(a))
        print(type(b))
        print(dir(a))
        print(dir(b))


def graph(lines, start=-50, stop=50):
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    x = list(range(start, stop))
    for line in lines:
        y = [line.f(i) for i in x]
        ax.plot(x, y, linewidth=2)

    ax.set_aspect('equal')
    plt.show()


def max_line(start, lines, x_min):
    m_line = None
    m_y = -float('inf')
    for line in lines:
        if line != start:
            x, y = solution(start, line)
            if y > m_y and x > x_min:
                m_line = line
                m_y = y
    return m_line


def visible(lines):
    print(f'{lines = }')
    out = []
    lines.sort(key=lambda x: x.m)

    out.append(lines[0])
    last_x = -float('inf')
    for line in lines[1:-1]:
        next_line = max_line(out[-1], lines, last_x)
        if next_line == None:
            break
        last_x = solution(next_line, out[-1])[0]
        print(f'adding {next_line.name} because it has the highest soln on {out[-1].name}')
        out.append(next_line)
    if lines[-1] not in out:
        out.append(lines[-1])
    return out



if __name__ == '__main__':
    a = Line(-8, -20, name='a')
    b = Line(-1/2, -3, name='b')
    c = Line(-1/5, -3/2, name='c')
    d = Line(3/2, -7, name='d')
    e = Line(3, -14, name='e')
    lines = [a, b, c, d, e]

    # graph(lines, start=-10, stop=10)

    visible = visible(lines)
    print([x.name for x in visible])
    print(len(visible))
