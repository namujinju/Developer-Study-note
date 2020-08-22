# def isValid(s):
#     while "()" in s or "[]" in s or "{}" in s:
#         s = s.replace("()", "").replace("[]", "").replace("{}", "")
#     return s == ""

def isValid(s):
    stack = []
    lookup = {'(': ')', '{': '}', '[': ']'}

    for paren in s:  # s를 훑는다.
        if paren in lookup:  # 여는 괄호일 경우
            stack.append(paren)  # stack에 여는 괄호 추가

        # 닫는 괄호인 경우
        elif (paren in lookup.values()) and (not stack or lookup[stack.pop()] != paren):
            # stack에는 여는 괄호만 들어오는데 not stack은 저장된 여는 괄호 없이 닫는 괄호만 들어온 경우.
            # lookup[stack.pop()] != paren 은 stack의 마지막 여는 괄호에 대응하는 종류의 닫는 괄호와
            # 현재 훑고 있는 s의 닫는 괄호와 다른 경우 역시 False
            return False

    return not stack  # 여는 괄호인 채로 끝나는 경우


s = "[](ㅇ)"
print(isValid(s))
