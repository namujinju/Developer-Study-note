def solution(num):
    return sum(i for i in range(1, num) if i % 3 == 0 or i % 5 == 0)