dict_commanders = {
    "Zerg": "아바투르",
    "Terran": "멩스크",
    "Protoss": "피닉스"
}
print(dict_commanders["Protoss"])

dict_commanders["Protoss"] = "카락스"

print(dict_commanders["Protoss"])

dict_me = {
    "name": "나무진주", # 딕셔너리 정의할 때 콤마 잊지 말 것
    "age": "18"
}
dict_me["price"] = 5000
print(dict_me["age"])

# 딕셔너리 요소 제거
del dict_commanders["Zerg"]
print(dict_commanders)

# 딕셔너리 내부에 키가 있는지

# key = input("")
# if key in dict_commanders:
#     print("있는 키다")
# else:
#     print("없어!")

value = dict_commanders.get("Random") # 키가 존재하지 않을 때 None을 출력
print(value)

dict_unit1 = {
    "name": "Zergling",
    "Hp" : "35",
    "Attack" : "5"
}
for key in dict_unit1:
    print(key, ":", dict_unit1[key])

dict_a = {}
dict_a["name"] = "구름"
print(dict_a)
del dict_a["name"]
print(dict_a)

print("")

pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]
# for i in pets:
#     print(pets[i]["name"], str(pets[i]["age"]) + "살")

for i in pets:
     print(i)

for pet in pets:
    print(pet["name"], str(pet["age"]) + "살")
# pet에 리스트 요소 하나씩 총 네 번 돈다. 리스트 요소 하나가 
# 딕셔너리 하나.


numbers = [4,5,1,2,4,8,8,4,7,5,9,4,4,2,1,7,2,2,5,3,2,6,6,3,9,4,0]
counter = {}

for num in numbers:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

print(counter)

print("")

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is list:
        for i in character[key]:
            print(key, ":", i)
    elif type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    else:
        print(key, ":", character[key])

        
