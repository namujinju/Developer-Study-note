# Level 2 큰 수 만들기
# 시간 복잡도, 더 효율적인 코드 만들기
# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(number, k):
    answer = [i for i in number]
    count = 0
    i = 0
    while True:
        
        if answer[i] < answer[i+1]:
            answer.pop(i)
            count+=1
            i-=1
        i += 1

        if count == k: # k개 숫자를 없앤 경우
            break

        if i == len(answer) - 1: # 끝까지 다 훑은 경우
            break
                    
    while count != k:
        answer.pop()
        count+=1

    return "".join(answer)

# 모범 답안
def solution2(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


number = '477234523432452841'
k = 10

print(solution2(number, k))
