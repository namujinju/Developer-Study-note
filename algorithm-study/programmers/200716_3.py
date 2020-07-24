def solution(s):
    return s.lower().count("p") == s.lower().count("y")


s = "PpyY"
print(solution(s))