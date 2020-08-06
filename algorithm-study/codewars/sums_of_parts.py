def parts_sums(ls):
    dic = {}
    result = 0
    for i in range(len(ls)-1, 0-1, -1):
        result += ls[i]
        dic[i] = result
    return sorted(dic.values(), reverse=True)+[0]


ls = [23744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
print(parts_sums(ls))
