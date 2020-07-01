def collatz(n):
    m = n
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        counter += 1
        print("{} {}번째".format(int(n), counter)) # n이 어떤 과정을 거쳐 1이 되는지 확인
    return "{}에서 시작하면 {}번을 거쳐 1이 됩니다".format(m, counter)

n = int(input())

#for i in range(1, n + 1): # n까지의 자연수들이 모두 콜라츠 추측에 부합하는지 확인
#    print(collatz(i))

print(collatz(n)) # n이 어떤 과정을 거쳐 1이 되는지 확인
