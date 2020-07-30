# Level 2 쇠막대기
def solution(arrangement):
    sum, stack = 0, 0
    arr = [i for i in arrangement]

    for i in range(len(arr)):
        if arr[i] == "(":
            stack += 1
        else:
            stack -= 1
            a = "".join(arr[i-1:i+1])
            if a == "()":
                sum += stack
            else:
                sum += 1
    return sum


arrangement = "()(((()())(())()))(())"
print(solution(arrangement))
