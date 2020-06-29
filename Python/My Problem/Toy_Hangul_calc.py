#무엇 곱하기 무엇은? 무엇 더하기 무엇은? 하는 식의 한글 포함 계산기
# 숫자와 연산자는 공백으로 구분

# 숫자와 연산자 입력 받기
# # 더하기, 빼기, 곱하기, 나누기 연산자를 인식 후 계산
# ()은, ()는 구분하기

# a, b는 입력 숫자
# e : 연산자
# han_e : 한글 연산자
# han_zosa : 한글 조사 (은, 는)
# result : 결과값

a, e, b = input().split(" ")

if e == "+":
    han_e = "더하기"
    result = float(a) + float(b)
elif e == "-":
    han_e = "빼기"
    result = float(a) - float(b)
elif e == "/":
    han_e = "나누기"
    result = float(a) / float(b)
elif e == "*":
    han_e = "곱하기"
    result = float(a) * float(b)
else:
    print("연산자 똑바로 입력해라")
    han_e = "몰라"
    result = "몰라"

if b[-1] in "013678":
    han_zosa = "은"
else:
    han_zosa = "는"

print("{}".format(a), han_e, "{}".format(b), han_zosa, result)





