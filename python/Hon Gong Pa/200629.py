list_a = [1,2,3,4,5]
temp = reversed(list_a)

for i in reversed(list_a):
    print(i)

print(temp)


print("안녕하세요"[::-1])
list_ex = ["a", "b", "c"]

print(list(enumerate(list_ex)))

for i, value in enumerate(list_ex):
    print("{}번째 요소는 {}입니다".format(i, value))

print("")

dict_ex = {
    "키a": "값a",
    "키b": "값b",
    "키c": "값c"
}

print(dict_ex.items())

for key, element in dict_ex.items():
    print("{} {}".format(key, element))

