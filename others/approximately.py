import math

def update_hashing(h, k, low, high):
    values = h.get(k)
    if not values:
        h[k] = (low, high)
    else:
        h[k] = (min(values[0], low), max(values[1], high))


def build_approximately_hashing(A, ep):
    h = dict()
    for a in A:
        floor_a = math.floor(a)
