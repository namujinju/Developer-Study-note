# Level2 스킬트리

def solution(skill, skill_trees):
    
    answer = 0
    for skills in skill_trees:
        temp = 0
        for i in skill: # 단어 하나
            if i in skills:
                if temp <= skills.index(i):
                    temp = skills.index(i)
                else:
                    break
            else: # skill이 skills에 없는 경우 index값을 큰값으로 보냄
                temp = 2e64
        else:
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
