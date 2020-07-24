n = int(input())
list_p = list(map(int, input().split(" ")))
list_p.sort(reverse=True)
output = 0
for i in range(n):
    output += list_p[i] * (i + 1)

print(output)