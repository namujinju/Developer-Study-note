# Level 3 이중우선순위 큐
import heapq as hq
import time


def solution(operations):
    answer = []  # 최솟값
    ansrev = []  # 최댓값
    for operation in operations:
        value = int(operation[2:])
        if "I" in operation:
            hq.heappush(answer, value)
            hq.heappush(ansrev, -value)
        else:
            if answer:
                if value == 1:  # 최댓값 삭제
                    answer.remove(-hq.heappop(ansrev))
                else:
                    ansrev.remove(-hq.heappop(answer))
    if answer:
        max_val = -hq.heappop(ansrev)
        min_val = hq.heappop(answer)
    else:
        return [0, 0]

    return [max_val, min_val]


# operations = ["I 16", "D 1"]
# operations = ["I 7", "I 5", "I -5", "D -1"]
operations = ["I 16", "I -5643", "D -1",
              "D 1", "D 1", "I 123", "D -1", "I -5643"]
# operations = ["I -45", "I 653", "D 1", "I -642",
#               "I 45", "I 97", "D 1", "D -1", "I 333"]

start = time.time()

print(solution(operations))
print(time.time()-start)
