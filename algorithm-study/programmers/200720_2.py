# Level 3 종이접기

def solution(n):    
    if n == 1:
        return [0]
    return solution(n-1) + [0] + flip(solution(n-1))

def flip(arr):
    return list(map(lambda x: 0 if x == 1 else 1, arr))[::-1]


print(solution(3))