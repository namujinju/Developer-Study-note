# 땅따먹기
#
def solution(land):

    for i in range(len(land)-1):
        max_1 = sorted(land[i])[-1]
        max_2 = sorted(land[i])[-2]
        land[i+1] = list(map(lambda x: x+max_1, land[i+1]))
        land[i+1][land[i].index(max_1)] -= (max_1-max_2)

    answer = max(land[-1])
    return answer


land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(solution(land))
