def solution(arr):
    answer = [arr[i] for i in range(len(arr)) if arr[i:i+1] != arr[i+1:i+2]]

    return answer


arr = [1,1,3,3,0,1,1]
print(solution(arr))