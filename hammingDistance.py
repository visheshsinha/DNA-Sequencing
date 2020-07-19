# Hamming Distance 

def hammingDistance(x, y):
    distance = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            distance += 1
    return distance


# // editDistance(x, y) <= hammingDistance(x, y) when |x| = |y| (equal lengths)

# // editDistance(x, y) >= ||X| - |Y|| (atleast equal to absolute distance when x & y are of different lengths)