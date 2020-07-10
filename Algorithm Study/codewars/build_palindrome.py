def build_palindrome(s):
    for i in range(len(s)):
        if list(s[i:]) == list(reversed(s[i:])): # s의 오른쪽 끝부터 왼쪽 i번째까지 회문인지 검증
            s += "".join(reversed(s[:i]))
            return s
        elif list(s[:len(s)-i]) == list(reversed(s[:len(s)-i])): # s의 왼쪽 끝부터 len(s) - i번째까지 회문인지 검증
            s = "".join(reversed(s[len(s)-i:])) + s
            return s
        else:
            pass

s = "abdce"

print(build_palindrome(s))
