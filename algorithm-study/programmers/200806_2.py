# Level 2 주식 가격

def solution(prices):
    answer = []

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        else:
            answer.append(len(prices)-i-1)

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
