import heapq as hq
import sys

hq_arr = []
n = int(input())  # 연산 갯수

for _ in range(n):
    i = int(sys.stdin.readline())  # https://www.acmicpc.net/blog/view/56
    if i:
        hq.heappush(hq_arr, -i)
    else:
        if hq_arr:
            print(-hq.heappop(hq_arr))
        else:
            print(0)
