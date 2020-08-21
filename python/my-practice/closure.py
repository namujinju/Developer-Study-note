def foo():
    total = 0

    def sums(x):
        nonlocal total
        total += x
        return total

    return sums


c = foo()
print(c(1), c(2), c(3))

# 1 3 6
