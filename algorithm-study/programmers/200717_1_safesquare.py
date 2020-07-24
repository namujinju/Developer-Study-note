#멀쩡한 사각형

from math import gcd

def solution(w,h):
    g = gcd(w,h)

    return w*h - (w+h-g)

w = 8
h = 12

print(solution(w, h))