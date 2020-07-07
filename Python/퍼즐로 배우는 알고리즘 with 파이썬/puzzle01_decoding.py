def decoding(s):
    # 문자가 나올 때까지 달려
    # 문자가 나오면 인덱스 값 출력
    # 그 이전까지를 int로 변환해서 문자 곱하고 output에 저장
    # 그 문자 인덱스까지 s를 삭제
    # 반복문 break
    # s가 빈 문자열이 될 때까지 다시 시작

    output = ""
    i = 1
    while s != "":
        if s[i].isalpha():
            output += int(s[:i]) * s[i]
            s = s[i+1:]
            i = 1
        else:
            i += 1

    return output

s = "14k7g3w4s"
print(decoding(s))