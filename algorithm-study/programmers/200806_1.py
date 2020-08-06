# Level2 프린터

def solution(priorities, location):
    tup_list = []
    new = []

    for i, v in enumerate(priorities):
        tup_list.append((v, i))
    save = tup_list

    while tup_list:
        m = max(tup_list, key=lambda x: x[0])
        idx = tup_list.index(m)
        new.append(m)
        tup_list = tup_list[idx+1:] + tup_list[:idx]
        print("tup_list", tup_list, "new", new)

    return new.index((save[location][0], location)) + 1


priorities = [1, 1, 9, 1, 1, 1]
location = 0


print(solution(priorities, location))
