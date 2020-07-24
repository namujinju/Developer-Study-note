def ispalindrome(s):
    return [i for i in s] == [i for i in s[::-1]]

from collections import deque # 양방향 큐인 deque 함수 호출

graph = {}
graph["you"] = ["apple", "train", "game", "mouse"]
graph["mouse"] = ["cat", "monkey"]
graph["apple"] = ["grape"]
graph["grape"] = ["orange", "peach"]
graph["game"] = ["hp", "mp", "level"]
graph["train"] = []
graph["cat"] = []
graph["monkey"] = [] # 노드의 끝을 반드시 정의해줘야!! 이거 때문에 몇 시간을 고생함
graph["orange"] = []
graph["peach"] = []
graph["level"] = []
graph["hp"] = []
graph["mp"] = []

def search(name):
    search_queue = deque() # 새 큐를 생성
    
    search_queue += graph[name] # 모든 이웃을 탐색 큐에 추가
    searched = []

    while search_queue:
        word = search_queue.popleft()# pop(0)를 쓰면 오류가 생기는 이유? 큐는 인덱스로 호출할 수 없기 때문
        if word not in searched:
            if ispalindrome(word):
                print(word + "는 회문이다")
                return True
            else:
                search_queue += graph[word]
                searched.append(word)

    return False


search("you")





