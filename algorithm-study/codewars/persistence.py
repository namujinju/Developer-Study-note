#from math import prod // can't use

def persistence(n):
    count = 0
    while n > 9:
        mul = 1
        for i in str(n):
            mul *= int(i)
        n = mul
        count += 1
    return count
    

print(persistence(39))