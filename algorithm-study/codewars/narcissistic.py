def narcissistic(value):

    return sum([int(i) ** len(str(value)) for i in str(value)]) == value


value = 153
print(narcissistic(value))

