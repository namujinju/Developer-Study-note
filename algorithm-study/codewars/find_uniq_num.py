def find_uniq(arr):
    arr = sorted(arr)
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        if arr[0] == arr[-1]:
            return arr[1]
        else:
            return arr[0]
    return sorted(arr)[-1]

# 모범 답안
def find_uniq2(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

arr = [0, 0, 0.55, 0, 0]
print(find_uniq(arr))