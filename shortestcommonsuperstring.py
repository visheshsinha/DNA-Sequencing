from overlaps import overlap
import itertools

def scs(ss):
    shortest_sup = None
    for sspern in itertools.permutations(ss):
        sup = sspern[0]
        for i in range(len(ss) - 1):
            olen = overlap(sspern[i], sspern[i+1], min_length=1)
            sup += sspern[i+1][olen:]

        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup

    return shortest_sup

