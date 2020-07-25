# 라면 공장

import heapq as hq


def solution(stock, dates, supplies, k):
    heap_arr = []

    answer = 0
    idx = 0
    while stock < k:  # stock의 양이 끝나는 날까지 넉넉하면 종료
        for i in range(idx, len(dates)):  # 현재 stock으로 버틸 수 있는 dates 찾기
            if stock >= dates[i]:
                # 그 date의 supplies를 힙 배열에 추가
                hq.heappush(heap_arr, -supplies[i])
                idx += 1
            else:
                break

        stock -= hq.heappop(heap_arr)  # 최댓값을 stock에 더함
        answer += 1  # 공급받는 횟수 + 1

    return answer


stock = 2
dates = [1, 2, 6]
supplies = [3, 3, 7]
k = 15

print(solution(stock, dates, supplies, k))
