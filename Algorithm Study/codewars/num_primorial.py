def num_primorial(n):
    count, mul, i = 0, 1, 2

    while count != n:
        if isprime(i):
            mul *= i
            count += 1
        i += 1

    return mul

def isprime(n):

    if n<2:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

print(num_primorial(5))