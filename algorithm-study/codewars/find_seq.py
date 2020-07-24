def find_it(seq):
    a = {}

    for i in seq:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    print(a)
    for key, element in a.items():
        if element % 2 == 1:
            return key
    

a = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(a))

# 모범 답안

def find_it2(seq):
    return [i for i in seq if seq.count(i) % 2][0]

print(find_it2(a))