# Overlaps between pairs of reads

def overlap(x, y, min_length = 3):
    start = 0
    while True:
        start = x.find(y[:min_length], start)
        
        if start == -1:
            return 0

        if y.startswith(x[start:]):
            return len(x) - start

        start += 1


# Finding and representing all overlaps

from itertools import permutations

def naive_overlap_map(reads, k):
    olaps = {}
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > 0:
            olaps[(a, b)] = olen
    return olaps