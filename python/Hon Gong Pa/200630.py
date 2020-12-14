def factorial(n):
    
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print()


# 피보나치
# n = int(input())
# for i in range(1, n+1):
#     print(fibo(i))

# 메모화를 이용한 피보나치

dict_fibo = {
    1: 1,
    2: 1
}

def fibo(n):
    if n in dict_fibo:
        return dict_fibo[n]
    
    output = fibo(n-1) + fibo(n-2)
    dict_fibo[n] = output
    return output

print(fibo(50)) # 조기 리턴

print()


def flatten(data):
    output = []

    for i in data:
        if type(i) == list:
            output += flatten(i) # flatten(i)는 리스트라서 +로 연결.
        else:
            output.append(i) # i는 int라서 append하고, 

    return output
    

example = [[1, 2, 3], [4, [5, 6]], 7 ,[8, 9]]

print("원본:", example)
print("변환:", flatten(example))

print()

# 연습문제 2번
# 

# sol(100,2) = sol(98,2) + sol(97,3) + ... + sol(91,9) + sol(90,10)
peo_min = 2
peo_max = 10
peo_all = 100
memo = {}

def sol(peo_left, peo_sit):
    key = str([peo_left, peo_sit])

    #종료 조건
    if key in memo:
        return memo[key]

    if peo_left < 0:
        return 0

    if peo_left == 0:
        return 1
    
    # 재귀 처리
    count = 0
    for i in range(peo_sit, peo_max + 1):
        count += sol(peo_left - i, i)

    # 메모화 처리
    memo[key] = count
    # 종료
    return count

print(sol(100,2))