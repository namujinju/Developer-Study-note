def countBits(n):
    n = bin(n)
    return sum([int(i) for i in n[2:]])

# 참고
# count함수를 활용할 것

# def countBits(n):
#     return bin(n).count("1")