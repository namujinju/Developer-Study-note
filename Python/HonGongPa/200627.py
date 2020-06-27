# 파이썬은 변수에 자료형을 지정하지 않지만 TypeError가 발생할 확률이 높기 때문에
# 하나의 변수에는 되도록 하나의 자료형을 넣어 활용하는 것이 좋다.
string = "안녕하세요"
string += "!"
string += "!"
print(string)

# number = input("인사말을 입력하세요> ") # 사용자가 무엇을 입력해도 결과는 무조건 문자열 자료형이다.
# print(type(number))

a = input("첫 번째 숫자")
b = input("두 번째 숫자")
c = float(a) + int(b)
print(c)

a = input("첫 번째 글자")
b = input("두 번째 글자")
c = a + b
print(c)

output = str(52)
print(type(output))

#연습문제 6번
a = input("문자열 입력> ")
b = input("문자열 입력> ")
print(a, b) #튜플을 공부하기 전 스왑(swap)해보기 // 변수 교체
c = a
a = b
b = c
print(a, b) 