# 124 나라의 숫자
def solution(n):
    num = []
    if n == 0:
        return '0'
    else:
        while n:
            n, r = divmod(n, 3)

            if r == 0:
                r = 4
                n -= 1
            num.append(str(r))
    return "".join(reversed(num))


n = 10
print(solution(n))

