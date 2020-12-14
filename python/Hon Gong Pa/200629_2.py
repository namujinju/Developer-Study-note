output = [i for i in range(1, 100 + 1) if "{:b}".format(i).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))

print("합계:",  sum(output))


# def print_n_times(n):
#     for i in range(n):
#         print("하이")
# 
# n = int(input())
# print_n_times(n)


#가변 매개변수

def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "3", "d", "나무진주")

#기본 매개변수
def square(value, n = 2):
    print(value ** 2)

square(3)


def return_test():
    return
value = return_test()
print(value)


def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i

    return output

value = sum_all(4,7)
print(value)

def mul(*values):
    output = 1
    for value in values:
        output *= value

    return output

print(mul(5, 7, 9, 10))
print()

