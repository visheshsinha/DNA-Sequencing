def de_bruijn_ize(st, k):
    """ Return a list holding, for each k-mer, its left
        k-1-mer and its right k-1-mer in a pair """
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:i+k-1], st[i+1:i+k]))
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    return nodes, edges


# def visualize_de_bruijn(st, k):
#     """ Visualize a directed multigraph using graphviz """
#     nodes, edges = de_bruijn_ize(st, k)
#     dot_str = 'digraph "DeBruijn graph" {\n'
#     for node in nodes:
#         dot_str += '  %s [label="%s"] ;\n' % (node, node)
#     for src, dst in edges:
#         dot_str += '  %s -> %s ;\n' % (src, dst)
#     return dot_str + '}\n'