import string

dict_drink = {
    "Jabroni": "Patron Tequila",
    "School Counselor": "Anything with Alcohol",
    "Programmer": "Hipster Craft Beer",
    "Bike Gang Member": "Moonshine",
    "Politician": "Your tax dollars",
    "Rapper": "Cristal"
}

name = input("")
print(string.capwords(name))
if name not in dict_drink:
    print("Beer")
else:
    print(dict_drink[name])
