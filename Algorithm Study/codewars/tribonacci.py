def tribonacci(signature, n):

    memo = {}
    memo[0], memo[1], memo[2] = signature[0], signature[1], signature[2]

    for i in range(3, n):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return list(memo.values())[:n]

print(tribonacci([1, 1, 1], 1))
