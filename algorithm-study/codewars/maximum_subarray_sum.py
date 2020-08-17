from itertools import combinations


def max_sequence(arr):
    if arr:
        arr_list = [0]+[sum(arr[:i+1]) for i in range(len(arr))]
        sums_list = list(combinations(arr_list, 2))
        return max(max([y-x for x, y in sums_list]), 0)
    elif len(arr) == 1:
        return arr[0]

    else:
        return 0


arr = [1, 1, 1, 1, 1, 1, 1, 1, 1]

print(max_sequence(arr))
