from collections import Counter


def scramble(s1, s2):
    s1, s2 = sorted([s1, s2], key=lambda x: len(x))  # s1이 작은 길이 단어
    memo = {}
    for i in s2:
        if i in memo:
            memo[i] += 1
        else:
            memo[i] = 1

    for i in s1:
        if i in memo:
            if memo[i] == 0:
                return False
            else:
                memo[i] -= 1
        else:
            return False
    return True


s1 = 'cedewaraaossoqqyt'
s2 = 'codewars'
print(scramble(s1, s2))

# 모범 답안


def scramble2(s1, s2):
    return Counter(s2) - Counter(s1)


print(scramble2(s1, s2))
