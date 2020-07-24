pets = [
    {"name" : "구름", "age": 5},
    {"name" : "초코", "age": 3},
    {"name" : "아지", "age": 1},
    {"name" : "호랑이", "age": 1}
]

print("# 우리 동네 애완 동물들")

for i in range(4):
    print(pets[i]["name"], str(pets[i]["age"]) + "살")

print("")

for i in pets:
    print(i["name"], str(i["age"]) + "살")

for pet in pets:
    print("{} {}살".format(pet["name"], pet["age"]))

print("")



nums = [1,4,3,5,6,7,5,5,8,9,0,3,4,2,5,5,4,6,7,8,9,2,1,1,2,2,3]
counter = {}

for num in nums:
    if num not in counter:
        counter[num] = 1
    else:
        counter[num] += 1

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
    
    if type(character[key]) is dict:
        for small_key in character[key]:
            print("{} : {}".format(small_key, character[key][small_key]))
    
    elif type(character[key]) is list:
        for i in character[key]:
            print("{} : {}".format(key, i))
    else:
        print("{} : {}".format(key, character[key]))
    

