def valid_parentheses(s):
    output = 0

    for i in s:
        if i == "(":
            output += 1
        elif i == ")": 
            output -= 1
        else:
            pass
        
        if output < 0:
            return False
    
    if output != 0:
        return False
    return True
    

def valid_parentheses2(s):
    output = 0

    for i in s:
        if i == "(": output += 1
        if i == ")": output -= 1
        if output < 0: return False

    return True if output == 0 else False

# 조건문을 한 줄로 쓸 수 있다.
# ex)
# if output < 0: return False