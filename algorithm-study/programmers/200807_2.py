# Level 3 가장 긴 팰린드롬

def solution(s):
    for i in range(len(s), 1-1, -1):
        for j in range((len(s)-i+1)):
            if s[j:i+j] == s[j:i+j][::-1]:
                return i


s = "abcdcba"

print(solution(s))
