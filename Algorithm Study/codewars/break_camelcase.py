def solution(s):
    low_s = s.lower()

    list_i = []
    list_s = []

    for i in range(len(s)):
        if s[i] != low_s[i]:
            list_i.append(i)

    for i in s:
        list_s.append(i)
    
    for i in list_i:
        list_s.insert(i+list_i.index(i), " ")

    return "".join(list_s).strip()

#참고
#def solution(s):
#    return ''.join(' ' + c if c.isupper() else c for c in s)