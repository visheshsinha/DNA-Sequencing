# Recursive Implementation of editDistance (very slow) 

def editDistanceRecursive(x, y):
    if len(x) == 0:
        return len(y)
    elif len(y) == 0:
        return len(x)
    else:
        distHor = editDistanceRecursive(x[:-1], y) + 1
        distVer = editDistanceRecursive(x, y[:-1]) + 1
        if x[-1] == y[-1]:
            distDiag = editDistanceRecursive(x[:-1], y[:-1])
        else:
            distDiag = editDistanceRecursive(x[:-1], y[:-1]) + 1
        
        return min(distHor, distVer, distDiag)


# Dynamic Programming approach for editDistance (insanely fast)

def editDistance(x, y):
    D = []
    for i in range(len(x) + 1):
        D.append([0] * (len(y)+1))

    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = i

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    
    # Edit distance is the value in the bottom right corner of the matrix
    return D[-1][-1]

# editDistance for Approximate Matching with minimum edits

def editDistance_approx(x, y):
    D = []
    for i in range(len(x) + 1):
        D.append([0] * (len(y)+1))

    for i in range(1, len(x)+1):
        D[i][0] = i

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    
    return min(D[:][-1])