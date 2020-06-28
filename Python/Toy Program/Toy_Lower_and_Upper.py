# 대소문자 관계없이 영어 문자열을 입력했을 때 앞글자는 대문자, 뒷글자는 소문자로 변환하는 프로그램

# 문자열을 입력받는다(input).
# 문자열의 첫 글자를 따와서 Upper 시키고 변수에 저장한다.
# 첫 글자 이외를 따와서 Lower 시키고 변수에 저장한다.
# 두 변수를 합쳐서 출력한다.

str_x = input("영어 글자를 입력해라")

str_up = str_x[0].upper()
str_low = str_x[1:].lower()

print(str_up + str_low)
