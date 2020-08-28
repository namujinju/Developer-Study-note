def climbStairs(n):
    if n <= 2:
        return n

    arr = [1, 2]
    for i in range(n-2):
        arr.append(arr[-1]+arr[-2])
    return arr[n-1]


n = 4
print(climbStairs(n))
