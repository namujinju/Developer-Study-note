def solution(p):
    count = 0

    # 빈 문자열인 경우 빈 문자열로 return
    if p == "": return ""

    for i in range(len(p)):
        if p[i] == "(": count+=1
        if p[i] == ")": count-=1
        if count == 0:
            u = p[:i+1]
            v = p[i+1:]
            if u[0] == "(": # 올바른 문자열
                return u + solution(v)
            if u[0] == ")": # 올바르지 않은 문자열
                temp = "".join("(" if i == ")" else ")" for i in u[1:-1])
                return "(" + solution(v) + ")" + temp

    

        

p = "()))((()"
print(solution(p))

