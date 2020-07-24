
# Level2 기능개발

from math import ceil
from collections import Counter


def solution(progresses, speeds):
    answer = [ceil((100-progresses[0])/speeds[0])]

    for i in range(1, len(progresses)):
        answer.append(max(answer[i-1], ceil((100-progresses[i])/speeds[i])))
    return list(Counter(answer).values())

progresses = [30]
speeds = [30]	
print(solution(progresses, speeds))