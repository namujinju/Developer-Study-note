def find_missing_letter(chars):
    return chr(ord(chars[-1]) * (ord(chars[-1])+1) // 2 - (ord(chars[0])-1) * ord(chars[0]) // 2 - sum(list(map(lambda x: ord(x), chars))))
#  
chars = ["a","b","c","d","f"]
#  
print(find_missing_letter(chars))