def find_outlier(integers):
    mods = [i % 2 for i in integers]
    return integers[mods.index(1)] if mods.count(0) - 1 else integers[mods.index(0)]

integers = [2, 4, 0, 100, 4, 11, 2602, 36]

print(find_outlier(integers))

