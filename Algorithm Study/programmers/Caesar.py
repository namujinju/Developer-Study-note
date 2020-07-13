def solution(s, n):
    arr_upper = [chr(i) for i in range(65, 90+1)] * 2
    arr_lower = [chr(i) for i in range(97, 122+1)] * 2

    arr = arr_upper + arr_lower

    answer=""
    for i in s:
        if i.isalpha():
            answer += arr[arr.index(i)+n%26]
        else:
            answer += i

    return answer


s = "bD"
n = 4000
print(solution(s,n))