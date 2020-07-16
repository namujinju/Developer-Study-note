def solution(s):
    i = len(s)
    return s[(i-1)//2:i//2+1]

s = "abcd"
print(solution(s))