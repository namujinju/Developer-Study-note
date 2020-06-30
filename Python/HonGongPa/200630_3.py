a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

print()

# 변수 값을 교환하는 튜플

a, b = 1, 2
a, b = b, a

print(a)
print(b)


x, y = divmod(17,3)

print(x, y)

def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("하이")

call_10_times(print_hello)

numbers = [1,2,3,4,5,6]
print("::".join(str(i) for i in numbers))

list_a = [str(i) for i in numbers]
print(list_a)

print(2 ** 29)


print()

power = lambda x: x * x
under_3 = lambda x: x < 3

list_input = [1,2,3,4,5]
list_output = map(power, list_input)

print(list(list_output))

list_output = filter(under_3, list_input)

print(list(list_output))
print()

with open("basic.txt", "a") as file:
    file.write("\n텍스트 추가욤!")
    

with open("basic.txt", "r") as file:
    contents = file.read()

print(contents)
print()

