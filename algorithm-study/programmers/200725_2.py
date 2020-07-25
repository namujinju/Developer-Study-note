# Level 3 줄 서는 방법
from math import factorial as f


def solution(n, k):
    answer = []
    i = 1
    while i <= n:

        answer.append(i + (k-1) // f(n-1))
        k = (k-1) % f(n-i)
        i += 1
    return answer


n, k = 3, 5
print(solution(n, k))
