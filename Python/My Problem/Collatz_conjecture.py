def collatz(n):
    m = n
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1        
        counter += 1
        # print("{} {}번째".format(int(n), counter))
    return "{}에서 시작하면 {}번을 거쳐 1이 됩니다".format(m, counter)

n = int(input())
# n = 5

for i in range(1, n + 1):
    print(collatz(i))
# print(collatz(n))


