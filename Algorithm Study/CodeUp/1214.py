y, m = input().split(" ")
y = int(y)
m = int(m)

if (((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)):
    k = 29
else:
    k = 28

if m in [1, 3, 5, 7, 8, 10, 12]:
    n = 31 # n은 마지막 날
elif m == 2:
    n = k
else:
    n = 30

print(n)
