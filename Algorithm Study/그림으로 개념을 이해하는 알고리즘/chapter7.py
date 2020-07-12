    # 그래프 정의

graph = {}

graph["start"] = {} # 각 노드의 해시 테이블 정의
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 2
graph["a"]["d"] = 4

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["c"] = 7

graph["c"] = {}
graph["c"]["fin"] = 1

graph["d"] = {}
graph["d"]["c"] = 6
graph["d"]["fin"] = 3
graph["fin"] = {}


# costs 정의(가중치)

infinity = float("inf") # 무한 정의

costs = {}

costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# parents 정의

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None # 종료 조건

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    
    return lowest_cost_node


node = find_lowest_cost_node(costs) # 현재 costs에서 가장 싼 node를 선택, 초기값

while node is not None:
    
    neighbor = graph[node] # 해시 테이블

    for n in neighbor:
        new_cost = costs[node] + neighbor[n]

        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    
    processed.append(node)
    node = find_lowest_cost_node(costs)


print("최단 경로의 가중치:", costs["fin"]) # costs hash table의 fin키 값을 출력

# 여기까지가 책의 내용
# 질문: 경로 print는 어떻게?
# parents 해시 테이블에서 fin부터 역으로 올라간다. fin키의 값을 다시 키로 가지고 올라온다. 반복.

output = ["fin"]
key = "fin"

while key != "start": # start에 도달하면 끝
    key = parents[key]
    output.append(key)

#최단 경로 노드들 리스트
output = output[::-1]


#출력
print("최단 경로:", end=" ")
for i in output:
    print(i, end=" ")
    if i != "fin":
        print(end="--- ")





    



