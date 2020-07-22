# 공백으로 split
# 각 단어마다 첫째 글자는 ord, 둘째부터는 reverse해서 합치기
# " "으로 join하기

def encrypt_this(text):
    arr = text.split(" ")
    print(arr)

    return " ".join(map(small, arr))

def small(s):
    if s:
        s = [i for i in s]
        num = str(ord(s.pop(0)))

        if s:
            s[0], s[-1] = s[-1], s[0]
            return num + "".join(s)
        else:
            return num

    else: return ""

text = "A wise old owl lived in an oak"
print(encrypt_this(text))