def palindrome_chain_length(n):
    i = 0
    while n != int(str(n)[::-1]):
        n += int(str(n)[::-1])
        i += 1

    return i

n = 87
print(palindrome_chain_length(n))