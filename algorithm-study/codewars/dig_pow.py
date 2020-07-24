def dig_pow(n, p):
    output = 0
    for i, value in enumerate(str(n)):
        output += int(value) ** (p+i)
    return output / n if output % n == 0 else -1

print(dig_pow(92, 1))