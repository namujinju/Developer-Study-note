from collections import Counter

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for i in participant:
        dic[hash(i)] = i
        temp += int(hash(i))
    
    for i in completion:
        temp -= hash(i)

    answer = dic[temp]
    return answer

def solution2(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution2(participant, completion))

