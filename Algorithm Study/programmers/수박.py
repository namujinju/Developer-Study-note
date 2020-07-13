def solution(n):
    answer = '수박' * (n // 2) + '수'* (n % 2)
    return answer

n=3
print(solution(n))
