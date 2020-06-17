# Complete the strangeCounter function below.
def strangeCounter(t):
    c, i = 0, 0
    while c < t:
        c += 3 << i
        i += 1
    return c - t + 1


def strangeCounter2(t):
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2
    return rem-t+1
