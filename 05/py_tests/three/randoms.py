from script import Line, graph, solution
import matplotlib.pyplot as plt
import random



def solution(a, b):
    '''
    Find solution of two lines.
    Uses m and b values (from format y=mx+b)
    '''
    slopes = a.m - b.m
    offsets = b.b - a.b
    x = offsets / slopes
    y = a.f(x)
    return (x, y)

def b_visible(a, b, c):
    '''
    Checks that the line with middle slope (b) is visible
    '''
    x, y = solution(a, c)
    return b.f(x) > y

def visible(lines):
    '''
    Takes in a list of lines.
    Lines have values m and b (to fit format y=mx+b)
    Value on a line at x can by found by line.f(x) (to fit format f(x)=mx+b)
    '''
    lines.sort(key=lambda x: x.m)
    return visible_rec(lines)

def visible_rec(lines):
    '''
    Recursive function to find solutions
    '''
    # Base cases
    if len(lines) <= 3:
        if len(lines) < 3:
            return lines
        else:
            a, b, c = lines
            if b_visible(a, b, c):
                return lines
            else:
                return [a, c]

    middle = len(lines)//2

    # Recurse down to find solutions to sub problems
    # alpha = 2; beta = 2
    left = visible_rec(lines[:middle])
    right = visible_rec(lines[middle:])

    combined = left.copy()
    for line in right:
        combined.append(line)

        # Check if new line "hides" previous lines O(n)
        last_removed = True
        while last_removed:
            if len(combined) >= 3:
                a, b, c = combined[-3:]
                if not b_visible(a, b, c):
                    combined.remove(b)
                else:
                    last_removed = False
            else:
                last_removed = False

    return combined


n = 22
lines = []
angles = []
offs = []

###################################################
### Random Lines ###

slope = 80
min_slope, max_slope = -slope, slope
off = 50
min_off, max_off = -off, off

while len(lines) < n:
    s = int(random.random() * (max_slope - min_slope) + min_slope)
    if s not in angles:
        o = int(random.random() * (max_off - min_off) + min_off)
        lines.append(Line(s, o, name=str(len(lines))))
        angles.append(s)
        offs.append(o)
        print(s, o)

###################################################
### Constant test case for even number of nodes ###

# text = '''
# -37 38
# -26 21
# -63 41
# 62 -37
# -44 -9
# -15 48
# -68 -7
# -6 -48
# '''

# for row in text.strip().split('\n'):
#     s, o = row.strip().split(' ')
#     s = int(s)
#     o = int(o)
#     print(s, o)
#     lines.append(Line(s, o, name=len(lines)))
###################################################


vis = visible(lines)
print(vis)
print(len(vis), len(lines))
# graph(lines)
fig, ax = plt.subplots()
ax.set_xlabel("slopes")
ax.set_ylabel("offsets")
for line in lines:
    if line in vis:
        ax.scatter(line.m, line.b, color='red')
    else:
        ax.scatter(line.m, line.b, color='blue')
    ax.annotate(line.name, (line.m, line.b))

fig, ax = plt.subplots()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
width = 10
x = list(range(-width, width))
for line in lines:
    y = [line.f(i) for i in x]
    ax.plot(x, y, label=line.name, linewidth=3)
plt.legend()
plt.show()