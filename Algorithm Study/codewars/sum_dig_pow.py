def sum_dig_pow(a,b):
    return [i for i in range(a, b+1) if is_sumpow(i)]

def is_sumpow(n):
    output = 0
    for i in range(len(str(n))):
        output += int(str(n)[i]) ** (i+1)
    return n == output

print(sum_dig_pow(1, 135))

# 모범 답안
def filter_func(n):
    return n == sum([int(value) ** (i+1) for i, value in enumerate(str(n))])


def sum_dig_pow2(a,b):
    return filter(filter_func, [i for i in range(a, b + 1)])