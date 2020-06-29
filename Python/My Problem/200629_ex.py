# [[1],[2,4],[3,6,9],[4,8,12,16],...] 배열을 만들어라.

n = int(input())
array = []

for k in range(1, n+1):
    small_array = [k * i for i in range(1,k+1)]
    array.append(small_array)

print(array)
