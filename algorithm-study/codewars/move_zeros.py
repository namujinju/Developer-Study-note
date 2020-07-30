def move_zeros(array):
    num = array.count(0) - list(map(lambda x: str(x), array)).count("False")
    return [i for i in array if str(i) == "False" or i != 0] + [0] * num


array = [1, False, 1, 0.0, 0, 1, 2, 0, 1, 3, "a"]

print(move_zeros(array))
