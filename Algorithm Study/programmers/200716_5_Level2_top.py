def solution(heights):
    answer = [0] * len(heights)

    for i in range(len(heights)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break
    return answer


heights = [32, 23, 2, 2, 3, 4, 3, 2]

print(solution(heights))
ret = [0,0,2,2,4]