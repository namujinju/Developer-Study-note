
list_a = ["234", 195, "나무진주", "스텟먼", "tychus"]

list_number = []
for item in list_a:
    try:
        float(item) # 여기서 숫자가 아닌 것들을 거름
        list_number.append(item)

    except:
        pass


print(list_number)

try:

    output = 10 + "개"
    int("하이")

except:
    print("예외 처리다.")

finally:
    print("finally 구문입니다")

print()

numbers = [52, 273, 157, 486]

number = 157

try:
    numbers.index(number)
    print("{}는 {}위치에 있다.".format(number, numbers.index(number)))

except:
    print("리스트 내부에 없다")

finally:
    print("어쨌든 실행은 됐네")


print()

try:
    int("강아지")

except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

print()

try:
    int("나무진주") # ValueError

    list_a = [1,2,3,4,5]
    list_a[5] # IndexError

    print(m) # NameError
    a = 10 + "개" # TypeError

except NameError as exception:
    print("exception:", type(exception))

except IndexError as exception:
    print("exception:", type(exception))

except ValueError as exception:
    print("exception:", type(exception))

except Exception as exception:
    print("미처 파악하지 못한 exception:", type(exception))



