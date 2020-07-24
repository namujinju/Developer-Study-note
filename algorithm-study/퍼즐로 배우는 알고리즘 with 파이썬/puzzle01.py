caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F', 'B', 'B', 'F', 'B', 'B', 'B']
cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']
# 1. 뒤집는 건 caps[0]와 반대인 모자만 뒤집으면 된다.
# 2. caps를 탐색하다가 이전 요소와 다른 게 있으면 그 인덱스 출력.
# 3. 그 인덱스는 뒤집어야 할 구간의 시작점이거나 끝점-1이다.
# 4. 그 둘을 구분하는 방법은 caps[0]와 같은지 판정하면 된다.
# 5. 다르면 시작점, 같으면 끝점 - 1
# 6. 중요! 입력 리스트의 제일 마지막에 원소를 추가해서, 마지막 구간도 출력될 수 있도록.



def onepass(caps):
    start, end = [], []
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                start.append(i)
            else: # 끝점
                end.append(i-1)

    for i in range(len(start)):
        print("People in position", start[i], end=" ")
        if start[i] == end[i]:
            print("flip your cap!")
        else:
            print("through", end[i], "flip your caps!")

onepass(caps)
