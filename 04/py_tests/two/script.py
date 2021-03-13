
def build(l, tie=None):
    '''
    Pair up neighboring values and keep them if they match.
    If a pair doesn't match it "cancels out".
    For odd arrs, leftover value is becomes the tie breaker.
    '''
    built = []
    stop = 2 * (len(l) // 2)
    for i in range(0, stop, 2):
        x = l[i]
        y = l[i+1]
        if x == y:
            built.append(x)

    if stop != len(l):
        tie = l[-1]

    return (built, tie)

def helper(l, tie=None):
    '''
    Recursively build the next array.
    Return the last tie breaker value once the array is empty.
    '''
    if len(l) == 0:
        return tie
    else:
        b, tie = build(l, tie)
        out = helper(b, tie)
        return out

def verify(l, x):
    '''
    Used to verify the output before returning in starter()
    '''
    total = 0
    for value in l:
        if value == x:
            total += 1
            if total >= (len(l)//2) + 1:
                return True

    return False

def starter(l):
    '''
    Calls the recursive func and verfies the return
    '''
    out = helper(l)
    if verify(l, out):
        return out
    else:
        return None



if __name__ == '__main__':
    import random

    one = "ABAAAABB"
    two = "AAAAAAAABBBB"
    three = "AABBCAAAACC"
    odd = "AABBB"
    cancels = "ABABC"
    longString = "AAABABAAAAABABAAABBAAAAABBBBAABAAAABBBABAAABBABABBBBBBBAABBBBAAABBBABABAABBBBABAAABBAAAABAAAABBBABBB"

    arr = [char for char in cancels]
    random.shuffle(arr)

    out = starter(arr)
    print(f'Array: {arr}')
    print(f'Maj output: {out}')