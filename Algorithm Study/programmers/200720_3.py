# Level 2 위장
from collections import Counter

def solution(clothes):
    return prod(map(lambda x: x+1, Counter([i[1] for i in clothes]).values()))-1

def prod(arr):
    mul = 1
    for i in arr:
        mul *= i
    return mul

