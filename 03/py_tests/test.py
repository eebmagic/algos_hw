import random

def make_matrix(text):
    out = [[char for char in line.strip()] for line in text.split('\n')]
    return out


def helper(matrix):
    explored = {x: False for x in range(len(matrix))}
    stack = []

    for ind in range(0, len(matrix)):
        if not explored[ind]:
            worker(matrix, ind, explored, stack)

    return stack


def worker(matrix, start, explored, stack):
    explored[start] = True
    for ind, value in enumerate(matrix[start]):
        if value == '1':
            if not explored[ind]:
                worker(matrix, ind, explored, stack)

    stack.insert(0, start)


if __name__ == '__main__':
    # Load matrix
    with open('one.txt') as file:
        content = file.read().strip()
    m = make_matrix(content)
    print(str(m).replace('], [', ']\n['))
    
    # Make topographical sorting
    out = helper(m)
    print(out)
