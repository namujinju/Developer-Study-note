# 0, 1, 2, 3, 4 숫자만을 사용해서 모든 자릿수가 연속되는 10자리 자연수의 갯수를 구하여라

list_digit = ['0','1','2','3','4']

def check_continuity(my_list, list_digit):
    return all(abs(list_digit.index(a)-list_digit.index(b)) == 1 for a, b in zip(my_list, my_list[1:]))

def deci_to_penta(n):
    m = ""
    n = int(n)
    for i in range(10):
        a = n % 5
        n = n // 5
        m += str(a)

    return m



counter = 0

for n in range(int('4444444444', 5) + 1):
    if check_continuity(deci_to_penta(n), list_digit):
        counter += 1
        print("{} {}회".format(deci_to_penta(n), counter))