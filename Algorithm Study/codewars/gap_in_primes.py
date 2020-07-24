def gap(g, m, n):
    list_a = [0]
    for num in range(m, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list_a.append(num)
                if list_a[1] - list_a[0] == g:
                    return [list_a[0], list_a[1]]
                else:
                    list_a.pop(0)
                    
print(gap(4, 130, 200))

