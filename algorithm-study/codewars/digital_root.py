def digital_root(n):

    while n >= 10:
        list_n = [int(i) for i in str(n)]
        n = sum(list_n)

    return n

print(digital_root(37))