# Exact Matching Naive Algorithm 

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences


# Also Counting Matching Complement Pairs (only once if complement is same)

def naive_with_rc(p, t):  
    occurrences = []
    r = reverseComplement(p)
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if r != p:
            for k in range(len(r)):
                if t[i+k] != r[k]:
                    match = False
                    break
        if match:
            occurrences.append(i)
    return occurrences


# Allowing Upto 2 mistmatches per occurance

def naive_2mm(p, t):  
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        unmatch = 0
        for j in rangei(len(p)):
            if t[i+j] != p[j]:
                unmatch += 1
                if unmatch > 2:
                    match = False
                    break
        if match:
            occurrences.append(i)
    return occurrences
