def find_missing_letter(chars):
    i=0
    while ord(chars[i]) == ord(chars[i+1]) - 1:
        i += 1
    return chr(ord(chars[i])+1)


    
#  
chars = ["a","b","c","d","f"]
#  
print(find_missing_letter(chars))