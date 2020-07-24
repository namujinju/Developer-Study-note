from math import log

def isPP(n):
    for m in range(2, int(n ** 0.5) + 1):
        
        k = round(log(n, m))
        if m ** k == n:
            return [m, k]