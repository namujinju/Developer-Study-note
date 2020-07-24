def thirt(n):
    arr = [1,10,9,12,3,4]

    total = sum([int(v) * arr[i%6] for i, v in enumerate(reversed(str(n)))])
    if n == total:
        return n
    return thirt(total)

n = 1234567


print(thirt(n))





