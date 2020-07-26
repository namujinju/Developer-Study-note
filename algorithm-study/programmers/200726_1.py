# Level 3 줄 서는 방법
from math import factorial as f


def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    while arr:
        idx, k = divmod((k-1), f(n-1))
        k += 1
        answer.append(arr.pop(idx))
        n -= 1
    return answer


n, k = 3, 5
print(solution(n, k))
