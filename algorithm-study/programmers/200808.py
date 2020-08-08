# 최댓값과 최솟값

def solution(s):
    s = [int(i) for i in s.split(" ")]
    return f"{min(s)} {max(s)}"


s = "-1 -2 -3 -4"
print(solution(s))
