def high(x):
    x = x.split(" ")
    result = list(map(ord_sum, x))

    return x[result.index(max(result))]


def ord_sum(word):
    return sum([ord(i)-96 for i in word])


x = 'man i need a taxi up to ubud'
word = "man"
print(ord_sum(word))
print(high(x))
