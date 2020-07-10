def countdown(i):
    print(i)
    if i == 1: # 기본 단계(base case)
        return
    
    else: # 재귀 단계(recursive case)
        countdown(i-1)

countdown(5)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    else:
        pivot = arr[0]
        
        less = [i for i in arr[1:] if i <= pivot] # arr[1:]는 pivot을 빼기 위한 작업
        
        greater = [i for i in arr[1:] if i > pivot]
        print(less, greater)

        return quicksort(less) + [pivot] + quicksort(greater)


arr = [89, 6, 3, 5,13,56,89, 30,44]

print(quicksort(arr))


def sums(arr):


    if arr == []:
        return 0
    return arr[0] + sums(arr[1:])


arr = [3, 2,3,4, 5]
print(sums(arr))


def countlist(arr):

    if arr == []:
        return 0
    return 1 + countlist(arr[1:])

arr = [1,2,3,4,5]
print(countlist(arr))


def maxlist(arr):

    if len(arr) == 2: # 기본 단계
        return arr[0] if arr[0] >= arr[1] else arr[1]

    sub_max = maxlist(arr[1:]) # 재귀 단계, 재귀 시키기 위한 식

    return arr[0] if arr[0] > sub_max else sub_max

    
arr = [1,2,31,4,5]
print(maxlist(arr))
