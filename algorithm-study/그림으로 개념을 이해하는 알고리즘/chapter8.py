# 근사 알고리즘
# 초기값 정의

states_needed = set(["wa", "mt", "id", "nv", "ut", "or", "ca", "az"]) # cover가 필요한 주

stations = {} # 방송국과 주의 관계를 해시 테이블로 정의
stations["k1"] = set(["id", "nv", "ut"])
stations["k2"] = set(["id", "mt", "wa"])
stations["k3"] = set(["or", "nv", "ca"])
stations["k4"] = set(["nv", "ut"])
stations["k5"] = set(["az", "ca"])

final_stations = set() # 최종 방송국 집합 정의(최소 방송국으로 모든 주를 덮음)
# 여기에 best_station을 하나하나 추가해 간다.
# best_station이란?
# 현재 states_needed에서 가장 많이 덮을 수 있는 station


while states_needed:

    best_station = None
    
    states_covered = set()
    for station, states in stations.items(): # 한 바퀴, best_station 하나 찾기
        
        covered = states_needed & states # 현재 남은 주와 for 문으로 훑고 있는 정거장의 주 집합의 교집합
        if len(covered) > len(states_covered): #의 길이가 최대인 경우 best_station에 현재의 station을 대입
            states_covered = covered
            best_station = station

    states_needed -= states_covered # best_station 하나 찾으면 best_station:states_covered를 제외
    final_stations.add(best_station) # 최종 답에 best_station을 추가 후 반복

print(final_stations)
        

