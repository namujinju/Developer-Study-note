#이진 탐색
# list에서 item의 위치는?

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while high - low >= 0:
        mid = (low + high) // 2
        guess = list[mid]

        if guess < item:
            low = mid + 1
        elif guess == item:
            return mid
        else:
            high = mid - 1

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))
print(binary_search(my_list, 4))

print()

