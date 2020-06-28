limit = 10000
i = 1

sum_value = 0
while True:
    
    sum_value += i - 1
    i += 1

    if sum_value > limit:
        break
    


print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다"\
    .format(i-1, limit, sum_value))


max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i

    if i * j > max_value:
        max_value = i * j
        a = i
        b = j


print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

