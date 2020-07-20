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

# Dynamic Approach for reacting Overlap Graph for k-mer suffix overlap

from collections import defaultdict

def overlap_graph(reads, k):
    index = defaultdict(set)
    for read in reads:
        for i in range(len(read) - k + 1):
            index[read[i:i+k]].add(read)
            
    graph = defaultdict(set)
    for r in reads:
        for o in index[r[-k:]]:
            if r != o :                    # For avoiding counting overlapping the read to itself 
                if overlap(r, o, k):
                    graph[r].add(o)
    edges = 0
    for read in graph:
        edges += len(graph[read])
    return(edges, len(graph))