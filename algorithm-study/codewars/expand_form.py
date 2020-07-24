def expanded_form(num):
    rev_num = str(num)[::-1]
    arr = []
    for i, v in enumerate(rev_num):
        n = int(v)*10**(i)
        if n:
            arr.append(str(n))
    
    return " + ".join(reversed(arr))

num = 70304
print(expanded_form(num))