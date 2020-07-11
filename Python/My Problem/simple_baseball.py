# 매우 간단한 야구게임

import random

ans = "{:04d}".format(random.randrange(9999 + 1)) # 0 ~ 9999까지 랜덤 수, 0을 포함한 네 자리 숫자
print("답:", ans, "-> 테스트용")
ans = [i for i in ans] # 답 숫자의 각 자리 리스트화
count = 0


while True:

    strike = 0
    ball = 0

    while True:
        try:
            n = input("네 자리 숫자를 입력하세요")
            if len(n) != 4: # 네 자리가 아닌 경우 오류
                raise IndexError
            break
        except:
            print("똑바로 입력하세요")
        

    n = [i for i in n] # 입력 숫자의 각 자리 리스트화

    for i in range(4):
        strike += (ans[i] == n[i]) # 리스트 요소 비교로 스트라이크 계산
    
    #0 ~ 9까지 i를 돌려서 ans와 n 각각의 i의 개수 구하고 적은 게 볼(임시)의 개수
    for i in range(9+1):
        i = str(i)
        ball += min(ans.count(i), n.count(i))
    
    ball -= strike # 볼(임시)에서 스트라이크 제외

    print("{}스트라이크 {}볼".format(strike, ball))
    count += 1
    if strike == 4:
        break

print("{}회의 시도로 답을 맞췄습니다!".format(count))

