# sort the odd


def sort_array(arr):
    index_arr = []
    odd_arr = []

    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            index_arr.append(i)
            odd_arr.append(arr[i])
    
    odd_arr.sort()

    for i in range(len(index_arr)):
        arr[index_arr[i]] = odd_arr[i]

    return arr

arr = [5, 3, 2, 8, 1, 1, 4]

print(sort_array(arr))

# 모범 답안
# 파괴적 함수, pop, list comprehension, sorted 문법