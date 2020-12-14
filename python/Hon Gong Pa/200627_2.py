#2-4 숫자와 문자열의 다양한 기능
a = "{}".format(10)
b = "{} {}".format(10, 20)
print(type(a))
print(a)
print(b)

#문자열의 format() 함수
dokki = "네 도끼가 {}도끼냐 {}도끼냐 {}도끼냐".format("금", "은", "싸구려")
print(dokki)
d = "{}".format(True)
print(d)

# 정수를 특정 칸에 출력하기
a = "{} {}".format(1, 3, 5)
print(a)

a = "{:3d}".format(52)
print(a)

#기호 붙여 출력하기
a = "{:+d}".format(52)
b = "{: d}".format(52)
c = "{:+d}".format(-52)
d = "{:+d}".format(-52)
print(a)
print(b)
print(c)
print(d)

#조합해보기
a = "{:+5d}".format(52)
print(a)
a = "{:=+5d}".format(52)
print(a)
a = "{:+05d}".format(52)
print(a)
a = "{:+05d}".format(-52)
print(a)

#부동 소수점 출력
a = "{:15.3f}".format(4564.3444)
print(a)

a = "{:+015.3f}".format(4564.3444)
print(a)

#의미 없는 소수점 제거
a = 77.0
b = "{:g}".format(a)
print(b)

#대소문자 바꾸기
a = "Hello Work!"
print(a.upper())
a = "Hello Work!"
print(a.lower()) #비파괴적 함수이다. 원본을 변화시키지 않는 함수.

#다양한 문자열 기능
a = """
   하이욤  
구래    
    """
print(a.strip())

print("Namujinju".isalpha())
print("Namujinjuㅇ".isalpha())
print("Namujinju".islower())
print("namujinju".islower())
print("234".isdecimal()) #문자열이 정수 형태인지 확인

#문자열 찾기
a = "안녕안녕하세요".find("안녕")
print(a)
a = "안녕안녕하세요".rfind("안녕")
print(a)
a = "안녕안녕하세요".rfind("하")
print(a)

# in 연산자
print("하이" in "하이욤")
print("하이" in "Hello")

#split()
# 문자열을 특정한 문자로 자름

a = "kdsnwj7avalv7najbd7sjkf".split("7")
print(a)

#연습문제 3번
a = input("> 1번째 숫자: ")
b = input("> 2번째 숫자: ")
print()

print("{} + {} = {}".format(a, b, int(a)+int(b)))
