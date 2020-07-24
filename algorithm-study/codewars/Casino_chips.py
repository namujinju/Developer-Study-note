def solve(arr):
    a, b, c = sorted(arr)
    if a + b <= c : return a + b
    else: return (b + c - a) // 2 + a
        

arr = [12,12,12]

print(solve(arr))