def count(s):
    dict_sol = {}
    for i in s:
        if i in dict_sol:
            dict_sol[i] += 1
        else:
            dict_sol[i] = 1
    return dict_sol

# 나는 string의 문자 요소 하나하나 세서 더하며 dictionary에 추가했다.
# 다른 사람은 더하는 게 아니라 세서 '대입'한 dictionary를 정의해 return했다.