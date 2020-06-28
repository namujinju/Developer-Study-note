# a = input("").title()
# print(a)
# range(5)

array = [34, 61, 40, 904, 403]
for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))

for i in range(4, -1, -1):
    print("변수 = {}".format(i))

i = 0
while i < 10:
    print("{}번째 반복".format(i))
    i += 1


list_test = [1,2,3,1,2,3,4,1,2,3,5]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)

import time
num = 0
tick = time.time() + 3

while time.time() < tick:
    num += 1
print("{}번 반복".format(num))