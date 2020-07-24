a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)
list_t = [a, b, c]
list_t.sort()
if (0 < list_t[2] < list_t[0] + list_t[1]):
    print("yes")
else:
    print("no")