def comp(arr1, arr2):
    try:
        return sorted(arr2) == sorted([i*i for i in arr1])
    except:
        return False

#a = [121, 144, 19, 161, 19, 144, 19, 11]
#b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
#print(comp(a, b))

a = None
b = []
print(comp(a,b))