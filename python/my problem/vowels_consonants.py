# 문자열 "s"가 주어진다.
# 문자열의 각 문자를 자음이면 오름차순, 모음이면 내림차순으로 정렬해 재배치해라.
# 조건
# 1) 정렬은 대소문자 구분 없이 한다.
# 2) 자음들의 위치와 모음들의 위치는 바뀌지 않는다.
# 3) 공백의 위치는 그대로이다.
# 4) s는 빈 문자열이 아니며, 모든 문자는 영어로 입력된다.

def vowels_consonants(s):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    #s의 자음과 모음 리스트를 출력해 오름차순 정렬
    s_vowels = list(sorted([i for i in s if i in vowels]))
    s_consonants = list(sorted([i for i in s if i not in vowels and i.isalpha()], key = lambda x: str.lower(x)))

    output = []

    for i in s:
        if i in vowels:
            output.append(s_vowels.pop()) # 모음인 경우 오름차순 된 리스트의 맨 끝을 출력
        elif i == " ":
            output.append(" ")
        else:
            output.append(s_consonants.pop(0)) # 자음인 경우 오름차순 된 리스트의 맨 앞을 출력

    return "".join(output)


# 테스트와 출력
s = "Arcturus Mengsk"
print(vowels_consonants(s))
