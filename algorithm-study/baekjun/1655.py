import heapq as hq
import sys

n = int(input())
arr = []
min_heap = []

for _ in range(n):
    answer = []
    i = int(sys.stdin.readline())
    arr.append(i)

    for j in arr:
        hq.heappush(min_heap, j)
    for j in range(len(min_heap)):
        answer.append(hq.heappop(min_heap))

    print(answer[(len(answer)-1)//2])
