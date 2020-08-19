# 숫자의 표현
# from itertools import combinations as comb


# def solution(n):
#     arr = [i*(i+1)//2 for i in range(n+1)]
#     return len([y-x for (x, y) in comb(arr, 2) if y-x == n])
# 시간 초과


def solution(n):
    answer = 0
    sums = 0
    arr = []
    i = 1
    while i <= n+1:
        if sums > n:
            sums -= arr.pop(0)
        elif sums == n:
            answer += 1
            arr.append(i)
            sums += i
            i += 1
        else:
            arr.append(i)
            sums += i
            i += 1

    return answer


n = 15
print(solution(n))
