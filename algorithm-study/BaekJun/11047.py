output = 0
n, k = map(int,input().split(" "))
a = []

for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)

for i in range(n):
    output += k//a[i]
    k = k % a[i]

print(output)


