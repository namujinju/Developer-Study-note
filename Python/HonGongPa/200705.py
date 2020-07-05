key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", "200", "30", "5"]

character = {}

for i in range(4):
    character[key_list[i]] = value_list[i]

print(character)

print()

limit = 10000
i = 1

sum_value = 0
while sum_value <= 10000:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

print()

def mul(*values):
    output = 1
    for i in values:
        output *= i
    return output

print(mul(5,7,9,10))


print()

def flatten(data):
    output = []
    for i in data:
        
        if type(i) == list:
            output += flatten(i) # 리스트라서 + 로 각 요소를 연걸
        else:
            output.append(i) # 리스트가 아니라서 append로
    return output

example = [[1,2,3], 4, 5, [6,7,[8,9]]]

print("원본:", example)
print("변환:", flatten(example))
