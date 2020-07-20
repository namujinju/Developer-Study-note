# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    weight_sum, answer = 0, 0 # weight_sum은 현재 다리의 무게의 합

    while len(truck_weights) != 0 or weight_sum != 0: # 대기 트럭이 없고 다리에도 트럭이 없을 때 반복 종료
        
        weight_sum -= bridge.pop(0) # 다리를 지나가는 트럭이 빠져나옴
        if len(truck_weights) != 0: # 대기 트럭 배열이 빈 배열이 아니어야 IndexError가 안남
            if weight_sum + truck_weights[0] <= weight: # 대기 1번 트럭이 지나갈 수 있는지 확인
                weight_sum += truck_weights[0]
                bridge.append(truck_weights.pop(0))
                
            else:
                bridge.append(0)
        answer += 1

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))