from shortestcommonsuperstring import scs
from overlaps import overlap

import itertools

def pick_maximal_overlaps(reads, k):
    reada , readb = None, None
    best_olen = 0
    for a,b in itertools.permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

def greedy_scs(reads, k):
    reada, readb, olen = pick_maximal_overlaps(reads, k)
    while olen > 0:
        reads.remove(reada)
        reads.remove(readb)
        reads.append(reada + readb[olen:])
        reada, readb, olen = pick_maximal_overlaps(reads, k)
    return ''.join(reads)