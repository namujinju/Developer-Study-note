import heapq as hq
import sys

hq_arr = []
n = int(input())  # 연산 갯수

for _ in range(n):
    i = int(sys.stdin.readline())
    if i:
        hq.heappush(hq_arr, (abs(i), i))
    else:
        if hq_arr:
            print(hq.heappop(hq_arr)[1])
        else:
            print(0)
