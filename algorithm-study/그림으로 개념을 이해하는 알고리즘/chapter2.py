def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):

    newarr = []
    for i in range(len(arr)):
        newarr.append(arr.pop(find_smallest(arr)))
    
    return newarr


arr = [7,5,6,3,9,2]
print(selection_sort(arr))