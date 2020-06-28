i = 0

while True:
    print("{}번째 반복".format(i))
    i += 1
    input_text = input("종료할까? y: ")
    if input_text in ['y', 'Y']:
        print("반복 종료")
        break

print("")

numbers = [3, 4, 7, 9, 66, 1, 56, 100, 25]

for num in numbers:
    if num < 10:
        continue
    print(num)

key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

i = 0

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]





print(character)
