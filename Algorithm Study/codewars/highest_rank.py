def highest_rank(arr):
    maxi = 0
    for i in range(len(arr)):
        if arr.count(arr[i]) > arr.count(maxi):
            maxi = arr[i]
        elif arr.count(arr[i]) == arr.count(maxi):
            maxi = max(maxi, arr[i])
    return maxi

def highest_rank2(arr):
    return list(sorted(arr, key = lambda x: (arr.count(x), x)))[-1]


arr = [12, 12, 12, 12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 10]


print()
print(highest_rank2(arr))