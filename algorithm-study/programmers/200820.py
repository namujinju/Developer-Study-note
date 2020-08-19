# 숫자의 표현
# from itertools import combinations as comb


# def solution(n):
#     arr = [i*(i+1)//2 for i in range(n+1)]
#     return len([y-x for (x, y) in comb(arr, 2) if y-x == n])
# 시간 초과

# 1
# 1 + 2
# 1 + 2 + 3
# 1 + 2 + 3 + 4 < 15

# 1 + 2 + 3 + 4 + 5 == 15 -> answer += 1

# 1 + 2 + 3 + 4 + 5 + 6 > 15 -> 1 제거
# 2 + 3 + 4 + 5 + 6 > 15 -> 2 제거
# 3 + 4 + 5 + 6 > 15 -> 3 제거

# 4 + 5 + 6 == 15 -> answer += 1


def solution(n):
    answer = 0
    sums = 0
    arr = []
    i = 1
    while i <= n+1:
        if sums > n:
            sums -= arr.pop(0)
            continue
        elif sums == n:
            answer += 1

        arr.append(i)
        sums += i
        i += 1

    return answer


n = 15
print(solution(n))
