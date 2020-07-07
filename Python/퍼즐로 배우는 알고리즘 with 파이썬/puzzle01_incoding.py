# 인코딩

def incoding(s):
    output = ""
    s = s + " "
    count = 0
    print(s)
    for i in range(1,len(s)):
        print(s[i], s[i-1])
        count += 1
        if s[i] != s[i-1]:
            output += str(count)
            count = 0
            output += s[i-1]

    return output

s = "yyyyyyyyyyyyyyxzzzzkkzya"
print(incoding(s))

