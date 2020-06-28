#시작 값(a), 등비(r), 몇 번째(n)

a, r, n = input().split(" ")

result = int(a) * int(r) ** (int(n) - 1)

print(result)