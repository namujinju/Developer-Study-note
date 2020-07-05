n = input()


if "0" in n and int(n) % 3 == 0:
    n = sorted([i for i in n], reverse=True)
    print("".join(n))
else:
    print(-1)