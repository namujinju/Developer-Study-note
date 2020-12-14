# for 반복문
for cha in "나무진주": # for 반복자 in 반복할 수 있는 것: 코드
    print(cha)

for i in range(10):
    print("사랑해")

array = [273, '나무진주', '타이커스']
for elem in array:
    print(elem)


numbers = [45, 67, 120, 13, 777, 339, 157]

for num in numbers:
    if num >= 100:
        print("- 100 이상의 수:", num)


for num in numbers:
    if num % 2 == 0:
        print("{}는 짝수입니다".format(num))
    else:
        print("{}는 홀수입니다".format(num))

list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
print(list_of_list[0][0])
print(list_of_list[0][1])
print(list_of_list[0][2])
print(list_of_list[1][0])
print(list_of_list[1][1])
print(list_of_list[1][2])
print(list_of_list[1][3])
print(list_of_list[2][0])
print(list_of_list[2][1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for num in numbers:
    output[num % 3 - 1].append(num)

print(output)

