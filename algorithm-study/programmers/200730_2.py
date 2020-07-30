# Level 3 타일 장식물
def solution(N):
    if N == 1:
        return 4
    if N == 2:
        return 6

    fibo = [1, 1]

    for i in range(N-2):
        k = fibo[-1] + fibo[-2]
        fibo.append(k)
    answer = ((fibo[-1] + fibo[-2]) + (fibo[-2] + fibo[-3])) * 2

    return answer
